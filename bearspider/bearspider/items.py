# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BearspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 我们只需要评论的数据
    comment = scrapy.Field()
