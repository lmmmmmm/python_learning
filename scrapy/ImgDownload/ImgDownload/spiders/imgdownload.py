import scrapy

from ImgDownload.items import ImgItem


class ImgDownload(scrapy.Spider):
    name = 'imgdownload'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImgItem()
        imgUrls = response.css('.post-content img::attr(src)').extract()
        item['imageUrl'] = imgUrls
        yield item
