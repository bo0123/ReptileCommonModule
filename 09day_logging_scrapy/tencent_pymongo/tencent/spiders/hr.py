# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent_pymongo.com']
    start_urls = ['http://hr.tencent_pymongo.com/position.php']

    def parse(self, response):
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item = TencentItem()
            item["title"] = tr.xpath("./td[1]/a/text()").extract_first()
            item["position"] = tr.xpath("./td[2]/text()").extract_first()
            item["publish_date"] = tr.xpath("./td[5]/text()").extract_first()
            yield item
        #找到下一页的url地址
        next_url = response.xpath("//a[@id='next']/@href").extract_first()
        if next_url != "javascript:;":
            next_url = "http://hr.tencent_pymongo.com/" +next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                # meta = {"item":item}
            )

    def parse1(self,response):
        response.meta["item"]


