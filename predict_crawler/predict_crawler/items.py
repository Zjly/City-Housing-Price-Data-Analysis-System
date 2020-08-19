# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PredictCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    unit_price = scrapy.Field()
    total_price = scrapy.Field()
    unit_type = scrapy.Field()
    area = scrapy.Field()
    towards = scrapy.Field()
    floor = scrapy.Field()
    address = scrapy.Field()
    year = scrapy.Field()
