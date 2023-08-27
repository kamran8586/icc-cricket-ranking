# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_title = scrapy.Field()
    product_image = scrapy.Field()
    product_price = scrapy.Field()
    product_rating = scrapy.Field()

class CricketItem(scrapy.Item):
    ranking = scrapy.Field()
    team = scrapy.Field()
    matches = scrapy.Field()
    points = scrapy.Field()
    rating = scrapy.Field()