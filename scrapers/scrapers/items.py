# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class News(scrapy.Item):
    rank = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()
    # image
    # weather?
