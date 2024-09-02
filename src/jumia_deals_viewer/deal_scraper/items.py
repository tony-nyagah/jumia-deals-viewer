# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DealScraperItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_image = scrapy.Field()
    old_price = scrapy.Field()
    product_link = scrapy.Field()
