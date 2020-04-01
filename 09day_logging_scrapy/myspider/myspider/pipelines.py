# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name=="itcast":
            item["hello"]="world"
        return item


class MyspiderPipeline02(object):
    def process_item(self, item, spider):
        print(item)
        return item
