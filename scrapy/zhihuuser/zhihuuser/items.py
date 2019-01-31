# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in=scrapy.Field()
import scrapy


class UserItem(scrapy.Item):
    name = scrapy.Field()
    avatar_url = scrapy.Field()
    allow_message = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    avatar_url_template = scrapy.Field()
    badge = scrapy.Field()
    employments = scrapy.Field()
    follower_count = scrapy.Field()
    gender = scrapy.Field()
    headline = scrapy.Field()
    id = scrapy.Field()
    is_advertiser = scrapy.Field()
    is_blocking = scrapy.Field()
    is_followed = scrapy.Field()
    is_following = scrapy.Field()
    is_org = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    url_token = scrapy.Field()
    user_type = scrapy.Field()
