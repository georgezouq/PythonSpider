import os
from scrapy import log
from scrapy.http import Request
from scrapy.contrib.pipeline.images import  ImagesPipeline

class WeiboImage(ImagesPipeline):
    """
        This is pipeline for download weibo image.weibo_image_path field is the image path which save in file system
    """
    def __init__(self,store_uri,download_func=None):
        self.images_store = store_uri
        super(WeiboImage,self).__init__(store_uri,download_func=None)

    def get_media_requests(self,item,info):
        if item.get('weibo_image_path'):
            yield Request(item['weibo_image_path'])

    def item_completed(self, results, item, info):
        if self.LOG_FAILED_RESULTS:
            msg = '%s found errors proessing %s' % (self.__class__.__name__,item)
            for ok,value in results:
                if not ok:
                    log.err(value,msg,spider=info.spider)

        image_paths = [x['path'] for ok,x in results if ok]
        image_path = list_first_item(image_paths)
        item['']