# -*- coding: utf-8 -*-
import scrapy
from scrapers.items import News


class InfobaeSpider(scrapy.Spider):
    name = 'infobae'
    allowed_domains = ['www.infobae.com']
    start_urls = ['http://www.infobae.com/']

    def start_requests(self):
        urls = [
            'http://www.infobae.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        """
        @url http://www.infobae.com/
        @returns items 5
        @scrapes rank text link
        """
        tops = response.xpath("//div[contains(@class, 'pb-f-global-most-read')]//aside//header")[:5]
        for rank, ml in enumerate(tops):
            yield News(
                rank=rank + 1,
                text=ml.css('a::text').extract_first(),
                link=ml.xpath('.//a/@href').extract_first()
            )
