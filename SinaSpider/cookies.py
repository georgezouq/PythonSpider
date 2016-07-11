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
    {'no': '18240461798', 'psw': 'huawei123456'},
    {'no': '18240461963', 'psw': 'huawei123456'},
    {'no': '18240461997', 'psw': 'huawei123456'},
    {'no': '18240461947', 'psw': 'huawei123456'},
    {'no': '15224460994', 'psw': 'huawei123456'},
    {'no': '13143535685', 'psw': 'huawei123456'},
    {'no': '13123598281', 'psw': 'huawei123456'},
    {'no': '17011981654', 'psw': 'huawei123456'},
    {'no': '13068175692', 'psw': 'huawei123456'},
    {'no': '18860543142', 'psw': 'huawei123456'},
    {'no': '17011981728', 'psw': 'huawei123456'},
    {'no': '17191682873', 'psw': 'huawei123456'},
    {'no': '14740488861', 'psw': 'huawei123456'},
    {'no': '18240458553', 'psw': 'huawei123456'},
    {'no': '18240459232', 'psw': 'huawei123456'},
    {'no': '18240466441', 'psw': 'huawei123456'},
    {'no': '13248329912', 'psw': 'huawei123456'},
    {'no': '13204257115', 'psw': 'huawei123456'},
    {'no': '18240466298', 'psw': 'huawei123456'},
    {'no': '17011981885', 'psw': 'huawei123456'},
    {'no': '15864384839', 'psw': 'huawei123456'},
    {'no': '15806982841', 'psw': 'huawei123456'},
    {'no': '15865785774', 'psw': 'huawei123456'},
    {'no': '17011980034', 'psw': 'huawei123456'},
    {'no': '18221221406', 'psw': 'huawei123456'},
    {'no': '15901910841', 'psw': 'huawei123456'},
    {'no': '18240318426', 'psw': 'huawei123456'},
    {'no': '13071431307', 'psw': 'huawei123456'},
    {'no': '18240309136', 'psw': 'huawei123456'},
    {'no': '15242015484', 'psw': 'huawei123456'},
    {'no': '13117964099', 'psw': 'huawei123456'},
    {'no': '15317182950', 'psw': 'huawei123456'},
    {'no': '13151105168', 'psw': 'huawei123456'},
    {'no': '13151105735', 'psw': 'huawei123456'},
    {'no': '13151105310', 'psw': 'huawei123456'},
    {'no': '15921297014', 'psw': 'huawei123456'},
    {'no': '17185114953', 'psw': 'huawei123456'},
    {'no': '18240304476', 'psw': 'huawei123456'},
    {'no': '15592359844', 'psw': 'huawei123456'},
    {'no': '13229235591', 'psw': 'huawei123456'},
    {'no': '17053226052', 'psw': 'huawei123456'},
    {'no': '18240345942', 'psw': 'huawei123456'},
    {'no': '13076467357', 'psw': 'huawei123456'},
    {'no': '13172567047', 'psw': 'huawei123456'},
    {'no': '18240319386', 'psw': 'huawei123456'},
    {'no': '18304051267', 'psw': 'huawei123456'},
    {'no': '13016673187', 'psw': 'huawei123456'},
    {'no': '18304061831', 'psw': 'huawei123456'},
    {'no': '18304061901', 'psw': 'huawei123456'},
    {'no': '18566769170', 'psw': 'huawei123456'},
    {'no': '13166376718', 'psw': 'huawei123456'},
    {'no': '13166213861', 'psw': 'huawei123456'},
    {'no': '13166036539', 'psw': 'huawei123456'},
    {'no': '15579874340', 'psw': 'huawei123456'},
    {'no': '13042550351', 'psw': 'huawei123456'},
    {'no': '15132333924', 'psw': 'huawei123456'},
    {'no': '18304061367', 'psw': 'huawei123456'},
    {'no': '18304061013', 'psw': 'huawei123456'},
    {'no': '18304060957', 'psw': 'huawei123456'},
    {'no': '18304061365', 'psw': 'huawei123456'},
    {'no': '18304060787', 'psw': 'huawei123456'},
    {'no': '13470677109', 'psw': 'huawei123456'},
    {'no': '18304060798', 'psw': 'huawei123456'},
    {'no': '13025296594', 'psw': 'huawei123456'},
    {'no': '17088605318', 'psw': 'huawei123456'},
    {'no': '18968405081', 'psw': 'huawei123456'},
    {'no': '17078331768', 'psw': 'huawei123456'},
    {'no': '18671231286', 'psw': 'huawei123456'},
    {'no': '17828418109', 'psw': 'huawei123456'},
    {'no': '15663483349', 'psw': 'huawei123456'},
    {'no': '15663482470', 'psw': 'huawei123456'},
    {'no': '15663483047', 'psw': 'huawei123456'},
    {'no': '15663482874', 'psw': 'huawei123456'},
    {'no': '15663480747', 'psw': 'huawei123456'},
    {'no': '15663467491', 'psw': 'huawei123456'},
    {'no': '18067012923', 'psw': 'huawei123456'},
    {'no': '18576718560', 'psw': 'huawei123456'},
    {'no': '15356576391', 'psw': 'huawei123456'},
    {'no': '15570064503', 'psw': 'huawei123456'},
    {'no': '13336957413', 'psw': 'huawei123456'},
    {'no': '15570124996', 'psw': 'huawei123456'},
    {'no': '18967404958', 'psw': 'huawei123456'},
    {'no': '15314955754', 'psw': 'huawei123456'},
    {'no': '18066228943', 'psw': 'huawei123456'},
    {'no': '15314954843', 'psw': 'huawei123456'},
    {'no': '13728671452', 'psw': 'huawei123456'},
    {'no': '13760443480', 'psw': 'huawei123456'},
    {'no': '13025298004', 'psw': 'huawei123456'},
    {'no': '13220639418', 'psw': 'huawei123456'},
    {'no': '18397305254', 'psw': 'huawei123456'},
    {'no': '15274273649', 'psw': 'huawei123456'},
    {'no': '18254485647', 'psw': 'huawei123456'},
    {'no': '18483651612', 'psw': 'huawei123456'},
    {'no': '13182944603', 'psw': 'huawei123456'},
    {'no': '13805282624', 'psw': 'huawei123456'},
    {'no': '13294934413', 'psw': 'huawei123456'},
    {'no': '13526441662', 'psw': 'huawei123456'}
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