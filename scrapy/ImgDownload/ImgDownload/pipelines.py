# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class ImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, spider):
        for imgurl in item['imageUrl']:
            yield Request(url=imgurl)
