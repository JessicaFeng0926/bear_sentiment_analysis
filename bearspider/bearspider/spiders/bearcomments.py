import re

import scrapy
import json
from scrapy import Request

from .. items import BearspiderItem

class BearSpider(scrapy.Spider):
    '''爬虫类，继承自scrapy.Spider'''
    # 爬虫程序的唯一标识
    name = 'bear'
    # 允许爬取的域名
    # allowed_domains = ['club.jd.com']
    # 爬虫开始的页面
    start_urls = []
    # 每页有10条数据，我要试着爬取前5000页共50000条数据
    for page in range(2):
        # url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=3017823&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%page
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10686704103&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%page
        start_urls.append(url)
  

    
    def parse(self, response):
        
        # 定义一个从jsonp中提取json样式字符串的re.complie对象
        pattern = re.compile(r'^.*?({.*})\);$')
        # 提取出来的内容看起来像json,但格式还是普通字符串
        json_like = pattern.search(response.text).group(1)
        # 现在是真正的json了
        json_str = json.loads(json_like)
        # 从json里提取出评论来,得到一个列表
        comments = json_str['comments']
        # 有可能这一页没有评论，所以两种情况都要考虑到
        if comments:
            for comment in comments:
                item = BearspiderItem()
                # 每个comment是一个字典
                item['comment'] = comment['content']
                # 把数据传回引擎
                yield item
    
