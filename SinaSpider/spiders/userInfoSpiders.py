#encoding:utf-8
import re
import datetime
import requests
from lxml import etree
from SinaSpider.initUserId import wbUserID
from scrapy.selector import Selector
from scrapy.http import Request
from SinaSpider.items import UserInfoItem

class Spider():
    name = "userInfoSpiders"
    host = "http://weibo.cn"
    start_urls = []
    for ID in wbUserID:
        start_urls.append("http://weibo.cn/%s/info" % ID)

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse)

    def parse(self,response):
        userInfoItem = UserInfoItem()
        selector = Selector(response)
        ID = re.findall('weibo\.cn/(\d+)', response.url)[0]
        text1 = ";".join(selector.xpath('body/div[@class="c"]/text()').extract())  # 获取标签里的所有text()
        nickname = re.findall(u'\u6635\u79f0[:|\uff1a](.*?);', text1)  # 昵称
        gender = re.findall(u'\u6027\u522b[:|\uff1a](.*?);', text1)  # 性别
        place = re.findall(u'\u5730\u533a[:|\uff1a](.*?);', text1)  # 地区（包括省份和城市）
        signature = re.findall(u'\u7b80\u4ecb[:|\uff1a](.*?);', text1)  # 个性签名
        birthday = re.findall(u'\u751f\u65e5[:|\uff1a](.*?);', text1)  # 生日
        sexorientation = re.findall(u'\u6027\u53d6\u5411[:|\uff1a](.*?);', text1)  # 性取向
        marriage = re.findall(u'\u611f\u60c5\u72b6\u51b5[:|\uff1a](.*?);', text1)  # 婚姻状况
        url = re.findall(u'\u4e92\u8054\u7f51[:|\uff1a](.*?);', text1)  # 首页链接

        userInfoItem["_id"] = ID
        if nickname:
            userInfoItem["NickName"] = nickname[0]
        if gender:
            userInfoItem["Gender"] = gender[0]
        if place:
            place = place[0].split(" ")
            userInfoItem["Province"] = place[0]
            if len(place) > 1:
                userInfoItem["City"] = place[1]
        if signature:
            userInfoItem["Signature"] = signature[0]
        if birthday:
            try:
                birthday = datetime.datetime.strptime(birthday[0], "%Y-%m-%d")
                userInfoItem["Birthday"] = birthday - datetime.timedelta(hours=8)
            except Exception:
                pass
        if sexorientation:
            if sexorientation[0] == gender[0]:
                userInfoItem["Sex_Orientation"] = "gay"
            else:
                userInfoItem["Sex_Orientation"] = "Heterosexual"
        if marriage:
            userInfoItem["Marriage"] = marriage[0]
        if url:
            userInfoItem["URL"] = url[0]

        urlothers = "http://weibo.cn/attgroup/opening?uid=%s" % ID
        r = requests.get(urlothers,cookies=response.request.cookies)
        if r.status_code == 200:
            selector = etree.HTML(r.content)
            texts = ";".join(selector.xpath('//body//div[@class="tip2"]/a//text()'))
            if texts:
                num_tweets = re.findall(u'\u5fae\u535a\[(\d+)\]', texts)  # 微博数
                num_follows = re.findall(u'\u5173\u6ce8\[(\d+)\]', texts)  # 关注数
                num_fans = re.findall(u'\u7c89\u4e1d\[(\d+)\]', texts)  # 粉丝数
                if num_tweets:
                    userInfoItem["Num_Tweets"] = int(num_tweets[0])
                if num_follows:
                    userInfoItem["Num_Follows"] = int(num_follows[0])
                if num_fans:
                    userInfoItem["Num_Fans"] = int(num_fans[0])
        yield userInfoItem

        urlFollows = "http://weibo.cn/%s/follow" % ID # 爬第一页关注,加入待爬取列表
        idFollows = self.getNextID(urlFollows,response.request.cookies)
        for ID in idFollows:
            url = "http://weibo.cn/%s/profile?filter=1&page=1" % ID
            yield Request(url=url, callback=self.parse)

    def getNextID(self,url,cookies):
        """ 打开url 爬去里面的个人信息 """
        IDs = []
        r = requests.get(url=url,cookies=cookies)
        if r.status_code == 200:
            selector = etree.HTML(r.content)
            texts = selector.xpath(
                u'body//table/tr/td/a[text()="\u5173\u6ce8\u4ed6" or text()="\u5173\u6ce8\u5979"]/@href')
            IDs = re.findall('uid=(\d+)', ";".join(texts), re.S)
            return IDs