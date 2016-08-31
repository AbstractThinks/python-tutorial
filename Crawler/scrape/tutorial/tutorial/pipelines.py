# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class testPipeline(object):
    # vat_factor = 1.15

    def process_item(self, item, spider):
        if item['movie_description']:
            item['movie_description'] = "address is:"+item['movie_description'][0]
            return item
        else:
            raise DropItem('Missing movie_description')

# 在配置文件中配置并启用

# ITEM_PIPELINES = {
#     'myproject.pipelines.PricePipeline': 300,
#     'myproject.pipelines.JsonWriterPipeline': 800,
# }

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('item_pipe.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item