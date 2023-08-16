# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LimitlessVgcScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PokemonItem(scrapy.Item):
    name    = scrapy.Field()
    usage   = scrapy.Field()
    players = scrapy.Field()
    wins    = scrapy.Field()
    losses  = scrapy.Field()