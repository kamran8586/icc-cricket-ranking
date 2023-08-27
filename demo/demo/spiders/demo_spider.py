import scrapy
from ..items import DemoItem

class DemoSpiderSpider(scrapy.Spider):
    name = "demo_spider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=mobile"]

    def parse(self, response):
        item = DemoItem()
        for result in response.css('.s-asin'):
            item['product_title'] = result.css('.a-color-base.a-text-normal::text').get()
            item['product_image'] = result.css('.s-image::attr(src)').get()
            item['product_price'] = result.css('.a-price-whole::text').get()
            item['product_rating'] = result.css('.a-size-small .puis-bold-weight-text').css('::text').get()
            yield item
