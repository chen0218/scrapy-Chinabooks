# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from china_books.items import ChinaBooksItem
from china_books.items import ChinaBooks1

class ChinaBooksPipeline(object):
    def process_item(self, item, spider):
        return item

class SaveBooksClassify(object):
    def process_item(self, item, spider):
        if isinstance(item,ChinaBooksItem):
            if not os.path.exists('所有图书信息'):
                os.mkdir('所有图书信息')
            if not os.path.exists('所有图书信息/'+item['classify']):
                os.mkdir('所有图书信息/'+item['classify'])
            if not os.path.exists('所有图书信息/'+item['classify']+'/'+item['classify1']):
                os.mkdir('所有图书信息/'+item['classify']+'/'+item['classify1'])
            with open('所有图书信息/所有详细分类.txt','a') as f:
                f.write(str(item['classify1']))
                f.write(str(item['url'])+'\n')
        return item

class SaveBooks(object):
    def process_item(self, item, spider):
        if isinstance(item,ChinaBooks1):
            if not os.path.exists('所有图书信息/'+item['book_mkdir']):
                os.mkdir('所有图书信息/'+item['book_mkdir'])
            with open('所有图书信息/'+item['book_mkdir']+'/test.txt','a',encoding='utf-8') as f:
                f.write('书籍网址:'+str(item['book_url'])+' , ')
                f.write('书籍标题:'+str(item['book_title'])+' , ')
                f.write('作者:'+str(item['book_author'])+' , ')
                f.write('出版时间:'+str(item['book_time'])+' , ')
                f.write('出版社:'+str(item['book_press'])+' , ')
                f.write('价格:'+str(item['book_price'])+' , ')
                f.write('折扣:'+str(item['book_discount'])+' , ')
                f.write('定价:'+str(item['book_pricetit'])+' , ')
                f.write('简介:'+str(item['book_jinajie'])+' , ')
                f.write('\n')
        return item

#保存单只股票当天交易明细


