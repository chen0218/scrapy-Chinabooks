# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaBooksItem(scrapy.Item):
    classify = scrapy.Field()#大类
    classify1 = scrapy.Field()    #小类
    url = scrapy.Field()   #每个类型的链接

class ChinaBooks1(scrapy.Item):
    book_mkdir = scrapy.Field() #书本保存路径
    book_url = scrapy.Field()   #书本链接
    book_title = scrapy.Field()   #书本名称
    book_author = scrapy.Field()   #书本作者
    book_time = scrapy.Field()   #书本发布时间
    book_press = scrapy.Field()   #书本出本社
    book_price = scrapy.Field()   #书本当前价格
    book_discount = scrapy.Field()   #书本折扣
    book_pricetit = scrapy.Field()   #书本定价
    book_jinajie = scrapy.Field()   #书本简介

