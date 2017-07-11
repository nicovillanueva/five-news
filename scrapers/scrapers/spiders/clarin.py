# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.selector import Selector


class ClarinSpider(scrapy.Spider):
    name = 'clarin'
    allowed_domains = ['www.clarin.com']
    start_urls = ['http://www.clarin.com/']

    def start_requests(self):
        # TODO: ke?
        urls = [
            'http://www.clarin.com/ondemand/eyJtb2R1bGVDbGFzcyI6IkNMQUNsYXJpbkNvbnRhaW5lckJNTyIsImNvbnRhaW5lcklkIjoidjNfY29sZnVsbF9ob21lIiwibW9kdWxlSWQiOiJtb2RfMjAxNzUxMTk4OTQ4NzA5IiwiYm9hcmRJZCI6IjEiLCJib2FyZFZlcnNpb25JZCI6IjIwMTcwNzEwXzAwNzAiLCJuIjoiNyJ9.json'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        """
        @url http://www.clarin.com/
        @returns items 5
        @scrapes rank text link
        """
        d = json.loads(response.body.decode().replace('(', '').replace(')', '')).get('data')
        s = Selector(text=d)
        for i, ml in enumerate(s.xpath('//article')[:5]):
            yield {
                "rank": ml.xpath('.//div[contains(@class, "number")]/text()').extract_first().strip(),
                "text": ml.xpath('.//h2/text()').extract_first().strip(),
                "link": s.xpath('//article/parent::div/@onclick')[i].extract().split('\'')[1]
            }
