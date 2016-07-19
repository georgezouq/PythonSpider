# encoding=utf-8
import json
import base64
import requests
import os

"""
输入你的微博账号和密码，可去淘宝买，一元七个。
建议买几十个，微博限制的严，太频繁了会出现302转移。
或者你也可以把时间间隔调大点。
"""
myWeiBo = [
    {'no': '13130472516', 'psw': 'huawei123456'},
    {'no': '17185848369', 'psw': 'huawei123456'},
    {'no': '18240461798', 'psw': 'huawei123456'}
]

# http://stackoverflow.com/questions/13030095/how-to-save-requests-python-cookies-to-a-file
"""
def readCookies():
    if os.path.exists('_cookie.tmp'):
        f = open('_cookie.tmp', 'rw')

        while 1:
            line = f.readline()
            if line:
                yield line
            else:
                return
        f.close()

def writeCookies(cookies):
    f = open('_cookie.tmp', 'a')

    for i in cookies:
        requests.utils.dict_from_cookiejar(i).
        print(i)
        f.write(str(i))
        f.write('\n')

    f.close()

"""


def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']

        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        r = session.post(loginURL, data=postData)
        jsonStr = r.content.decode('gbk')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print "Get Cookie Success!( Account:%s )" % account
            cookie = session.cookies.get_dict()
            cookies.append(cookie)
        else:
            print "Failed!( Reason:%s )" % info['reason']

    return cookies


cookies = getCookies(myWeiBo)
print "Get Cookies Finish!( Num:%d)" % len(cookies)