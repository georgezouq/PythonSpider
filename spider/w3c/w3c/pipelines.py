# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class W3CPipeline(object):
    def <string>init</string>(self):
        self.file=codecs.open('w3c.json','wb',encoding='utf-8')#打开文件
    def process_item(self,item,spider):
        line=json.dumps(item['title'],ensure_ascii=False)+'\t'
        line=line+json.dumps(item['link'],ensure_ascii=False)+'\t'
        line=line+json.dumps(item['desc'],ensure_ascii=False)+'\n'
        self.file.write(line)#写入文件

    def process_item(self, item, spider):
        return item
