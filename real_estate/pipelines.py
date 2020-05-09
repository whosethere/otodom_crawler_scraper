from pymongo import MongoClient
from scrapy import Request
from os import path
from pymongo import MongoClient
from scrapy.crawler import Settings
import logging


class BetGatheringPipeline(object):
        # collection = 'matches_results'

        # def __init__(self, mongo_uri, mongo_db):
        #     self.mongo_uri = mongo_uri
        #     self.mongo_db = mongo_db
        
        def __init__(self, mongo_uri, mongo_db):
            self.mongo_uri = mongo_uri
            self.mongo_db = mongo_db
        @classmethod

        def from_crawler(cls, crawler):
            return cls(
                mongo_uri = crawler.settings.get('MONGO_URI'),
                mongo_db = crawler.settings.get('MONGO_DB')
            )

        def open_spider(self, spider):
            self.client = MongoClient(self.mongo_uri)
            self.db = self.client[self.mongo_db]

        def close_spider(self, spider):
            self.client.close()

        def process_item(self, item, spider):
            collection = str(type(item).__name__.lower())
            self.db[collection].insert_one(dict(item))
            return item

