# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from scrapy.conf import settings
import pymongo



class ScrapZhengshenPipeline(object):
    def __init__(self):
        client=pymongo.MongoClient(settings['A'],settings['B'])
        db=client[settings['C']]
        self.collection=db[settings['D']]
    def process_item(self, item, spider):
        db_infos=[info['case_id'] for info in self.collection.find()]
        if dict(item)['case_id'] not in db_infos:
            self.collection.insert(dict(item))
        return item
    # def __init__(self):
    #     connection=pymongo.MongoClient(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])
    #     db=connection[settings['MONGODB_DB']]
    #     self.collection=db[settings['MONGODB_COLLECTION']]
    # def process_item(self,item,spider):
    #     self.collection.insert(dict(item))
    #     return item
