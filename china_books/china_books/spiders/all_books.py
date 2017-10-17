# -*- coding: utf-8 -*-
import scrapy
from china_books.items import ChinaBooksItem
from china_books.items import ChinaBooks1
from bs4 import BeautifulSoup
import re

class AllBooksSpider(scrapy.Spider):
    name = "all_books"
    allowed_domains = ["bookschina.com"]
    start_urls = ['http://www.bookschina.com/books/kind/sort.aspx'] 

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        item = ChinaBooksItem()
        classify_list = soup.find_all('h2')
        classify1_list = soup.find_all('ul')
#        for i in range(3):
        for i in range(len(classify_list)-1):
            classify = re.findall(re.compile(r'k">(.*?)</a'),str(classify_list[i+1]))[0]      #取出大的分类
            item['classify'] = classify.replace('/','-')    #去掉字符串中的/
            classify1_list1 = str(classify1_list[i+11]).split('</li>')
#            for j in range(3):
            for j in range(len(classify1_list1)-1):
                classify1 = re.findall(re.compile(r'k">(.*?)</a'),str(classify1_list1[j]))[0]
                item['classify1'] = classify1.replace('/','-')
                url_one = re.findall(re.compile(r'href="(.*?)"'),str(classify1_list1[j]))[0]
                url = 'http://www.bookschina.com'+url_one
                item['url'] = url
                mkdir = str(classify.replace('/','-'))+'/'+str(classify1.replace('/','-'))
                yield item
                yield scrapy.Request(url, callback=self.parse_all_books_page,meta={'url':url,'mkdir':mkdir})
        print('结束1')

    def parse_all_books_page(self, response):
        soup = BeautifulSoup(response.text,'lxml')
        page_all = soup.find_all('div',class_='paging')
        page_list = BeautifulSoup(str(page_all),'lxml').find_all('li')
        page_max = re.findall(re.compile(r'title=.*">(.*?)</a'),str(page_list[len(page_list)-2]))[0]
        page_url = re.findall(re.compile(r'href="(.*?)_0'),str(page_list[len(page_list)-2]))[0]
#        循环页码
        for i in range(int(page_max)):
            url = 'http://www.bookschina.com'+str(page_url) + '_0_0_11_0_1_'+str(i+1)+'_0_0/'
            yield scrapy.Request(url, callback=self.parse_all_books,meta={'url':url,'mkdir1':response.meta['mkdir']})
        print('结束2')


# 解析具体分来下的各本书籍信息
    def parse_all_books(self, response):
        item = ChinaBooks1()
        book_all = BeautifulSoup(response.text,'html.parser').find('div',class_='bookList')
        book_list = BeautifulSoup(str(book_all),'lxml').find_all('li')
        item['book_mkdir'] = response.meta['mkdir1']
        for book_one in book_list:
            book_url='http://www.bookschina.com' + str(re.findall(re.compile(r'href="(.*?)"'),str(book_one))[0])
            book_title = re.findall(re.compile(r'title="(.*?)"'),str(book_one))
            book_author = re.findall(re.compile(r'sbook=(.*?)"'),str(book_one))
            book_time = re.findall(re.compile(r'出版时间">(.*?)/'),str(book_one))
            book_press = re.findall(re.compile(r'出版时间.*blank">(.*?)</a>'),str(book_one))
            book_price = re.findall(re.compile(r'sellPrice">(.*?)</'),str(book_one))
            book_discount = re.findall(re.compile(r'discount">(.*?)</'),str(book_one))
            book_pricetit = re.findall(re.compile(r'定价.*">(.*?)</'),str(book_one))
            book_jinajie = re.findall(re.compile(r'recoLagu">(.*?)</'),str(book_one))
            item['book_url'] = book_url
            item['book_title'] = book_title
            item['book_author'] = book_author
            item['book_time'] = book_time
            item['book_press'] = book_press
            item['book_price'] = book_price
            item['book_discount'] = book_discount
            item['book_pricetit'] = book_pricetit
            if len(book_url) > 2:
                item['book_jinajie'] = book_jinajie
            else:
                item['book_jinajie'] = None
            yield item
        print(str(len(book_list)))
        print('结束3')

'''
将最后一个函数获取的HTML解析
先获取页码
http://www.bookschina.com/kinder/53110000_0_0_11_0_1_10_0_0/
倒数第三个10就是页码
然后循环去获取
将每种分类的书籍保存在相应的文件夹中


学习并练习css  xpath   beautifulsoup  正则
将数据保存到数据库或者excel（可以用pandas中的dataframe）
使用url管理器
在可能出现异常的地方加上异常管理
'''

