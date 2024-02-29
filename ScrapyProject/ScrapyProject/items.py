# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojectItem(scrapy.Item):
    num = scrapy.Field()
    company = scrapy.Field()
    symbol = scrapy.Field()
    ytd_rtn = scrapy.Field()
