# -*- coding: utf-8 -*-
import scrapy


class DiarioPopularSpider(scrapy.Spider):
    name = 'diariopopular'
    allowed_domains = ['https://www.diariopopular.com.ar/']
    start_urls = ['http://https://www.diariopopular.com.ar/']

    def start_requests(self):
        urls = [
            'https://www.diariopopular.com.ar/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        """
        @url https://www.diariopopular.com.ar/
        @returns items 5
        @scrapes rank text link
        """
        for i, ml in enumerate(response.xpath("//section[contains(@class, 'article-ranking')]//article")):
            n = ml.xpath('.//a')[1]
            yield {
                "rank": i + 1,
                "text": n.xpath('@alt').extract_first(),
                "link": n.xpath('@href').extract_first()
            }
