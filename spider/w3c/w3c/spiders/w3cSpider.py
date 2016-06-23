import scrapy
from scrapy.selector import selector
from w3c.items import W3CItem

class w3cSpider(scrapy.Spider):
    name='w3c_spider' #爬虫名称，命令行运行时要用到
    allowed_domains=['w3school.com.cn']
    start_urls=[
        "<a href="http://www.w3school.com.cn/xml/xml_syntax.asp">http://www.w3school.com.cn/xml/xml_syntax.asp</a>"
    ]
    def parse(self,response):#scrapy 根据爬取地址发送请求后调用parse进行数据提取
        sel=Selector(response)
        sites=sel.xpath('//div[@id="course"]/ul/li') #使用xpath提取页面信息
        for site in sites:
            item = W3CItem()
            title=site.xpath('a/@title').extract()
            link=site.xpath('a/@href').extract()
            desc=site.xpath('a/text()').expract()

            item['title']=title[0] #组织item数据
            item['link']=link[0]
            item['desc']=desc[0]
            yield item #返回item数据给pipeline使用
