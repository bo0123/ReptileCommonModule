# -*- coding: utf-8 -*-
import scrapy
import logging
logger = logging.getLogger(__name__)


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        # ret1=response.xpath("//div[@class='tea_con']//ul/li//text()").extract()
        li_list=response.xpath("//div[@class='tea_con']//ul/li")

        for li in li_list:
            item={}
            item["name"]=li.xpath(".//h3//text()").extract_first().strip()
            item["title"]=li.xpath(".//h4//text()").extract_first()
            logger.warning(item)
            yield item  #减少内存占用,不能返回列表

