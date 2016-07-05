# encoding=utf-8
BOT_NAME = ['tweetSpiders','userInfoSpiders']

SPIDER_MODULES = ['SinaSpider.spiders']
NEWSPIDER_MODULE = 'SinaSpider.spiders'

DOWNLOADER_MIDDLEWARES = {
    "SinaSpider.middleware.UserAgentMiddleware": 1,
    #"scrapy.downloadmiddlewares.httpproxy.HttpProxyMiddleware":110,
    #"SinaSpider.middleware.ProxyMiddleware":100,
    "scrapy_crawlera.CrawleraMiddleware":400,
    "SinaSpider.middleware.CookiesMiddleware": 402,
}


"""
CRAWLERA_ENABLED = True
CRAWLERA_USER = '7652666d26624b7dbe312a0056936a9e'
CRAWLERA_PASS = 'A123456789'
"""

# CONCURRENT_REQUESTS = 32
# CONCURRENT_REQUESTS_PER_DOMAIN = 32
# AUTOTHROTTLE_ENABLED = False
# DOWNLOAD_TIMEOUT = 600

ITEM_PIPELINES = {
    'SinaSpider.pipelines.pipelines.MongoDBPipleline': 300,
    'scrapy_redis.pipelines.RedisPipeline':400
}

LOG_LEVEL = 'DEBUG'



SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

REDIS_URL = "redis://60.205.95.103:6379"
#REDIS_HOST = 'localhost' # '60.205.95.103'
#REDIS_PORT = 6379

DOWNLOAD_DELAY = 1  # 间隔时间
COMMANDS_MODULE = 'SinaSpider.commands'
# CONCURRENT_ITEMS = 1000
# CONCURRENT_REQUESTS = 100
# REDIRECT_ENABLED = False
# CONCURRENT_REQUESTS_PER_DOMAIN = 100
# CONCURRENT_REQUESTS_PER_IP = 0
# CONCURRENT_REQUESTS_PER_SPIDER=100
# DNSCACHE_ENABLED = True
# LOG_LEVEL = 'INFO'    # 日志级别
# CONCURRENT_REQUESTS = 70
