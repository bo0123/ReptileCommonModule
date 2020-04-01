# -*- coding: utf-8 -*-
import scrapy


class Itcast02Spider(scrapy.Spider):
    name = 'itcast02'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        pass
