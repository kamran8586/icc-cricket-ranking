import scrapy
from ..items import CricketItem

class CricketSpider(scrapy.Spider):
    name = "cricket"
    allowed_domains = ["www.icc-cricket.com"]
    start_urls = ["https://www.icc-cricket.com/rankings/mens/team-rankings/odi"]

    def parse(self, response):
        item = CricketItem()
        for data in response.css('table.table tbody tr'):
            item['ranking'] = data.css('td::text').get()
            item['team'] =  data.css('td:nth-child(2) .u-hide-phablet::text').get()
            item['matches'] = data.css('td:nth-child(3)::text').get()
            item['points'] = data.css('td:nth-child(4)::text').get()
            item['rating'] = data.css('td:nth-child(5)::text').get()
            yield item