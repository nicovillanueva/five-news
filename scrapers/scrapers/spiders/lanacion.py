# -*- coding: utf-8 -*-
import scrapy


class LaNacionSpider(scrapy.Spider):
    name = 'lanacion'
    allowed_domains = ['www.lanacion.com']
    start_urls = ['http://www.lanacion.com/']

    def start_requests(self):
        urls = [
            'http://www.lanacion.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        """
        @url http://www.lanacion.com/
        @returns items 5
        @scrapes rank text link
        """
        for ml in response.xpath('//section[contains(@id, "ranking")]/article'):
            yield {
                "rank": ml.xpath(".//span/text()").extract_first(),
                "text": ml.xpath(".//a/text()").extract_first(),
                "link": ml.xpath(".//a/@href").extract_first()
            }
