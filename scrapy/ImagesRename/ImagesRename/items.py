# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagesItem(scrapy.Item):
    img_url = scrapy.Field()
    img_name = scrapy.Field()
