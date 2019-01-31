import scrapy

from ImagesRename.items import ImagesItem


class ImageRename(scrapy.Spider):
    name = 'imagerename'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html',
                  'http://lab.scrapyd.cn/archives/57.html'
                  ]

    def parse(self, response):
        item = ImagesItem()
        item['img_url'] = response.css(".post img::attr(src)").extract()
        item['img_name'] = response.css(".post-title a::text").extract_first()
        yield item
