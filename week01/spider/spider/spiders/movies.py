# -*- coding: utf-8 -*-
import scrapy


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        for i in range(0, 10):
            url = f'https://maoyan.com/films?showType=3&offset='{i*30}'
            yield scrapy.Request(url=url, callback=self.parse)

    
        # 解析函数
    def parse(self, response):
        pass
