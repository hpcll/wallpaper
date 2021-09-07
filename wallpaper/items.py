# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WallpaperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    objectId = scrapy.Field()
    largeImageUrl = scrapy.Field()
    # print(objectId)
