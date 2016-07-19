# encoding=utf-8
import base64
import random

from SinaSpider.cookies.cookies import cookies
from proxy_ip import PROXY
from user_agents import agents


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ 换Cookie """

    def process_request(self, request, spider):
        cookie = random.choice(cookies)
        request.cookies = cookie

class ProxyMiddleware(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXY)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_proxy']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic' + encoded_user_pass
            print "********* ProxyMiddleware have pass *************" + proxy['ip_port']
        else:
            print "********* ProxyMiddleware no pass ***************" + proxy['ip_port']
            request.meta['proxy'] = "http://%s" % proxy['ip_port']