# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from spider.items import SpiderItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):

        for i in range(0, 10):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):

        items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for movie_hover_info in soup.find_all('div', attrs={'class': 'movie-hover-info'}):

            item = SpiderItem()

            for movie_name in movie_hover_info.find_all('span',attrs={'class':'name'}):
                movie_title = movie_name.text
                
            for movie_tag in movie_hover_info.find_all('div'):
                for movie_span_tag in movie_tag.find_all('span',attrs={'class':'hover-tag'}):
                    if movie_span_tag.text == '类型:':
                        movie_type = movie_tag.text.replace(' ','').replace('\n','').replace('类型:','')
                    elif movie_span_tag.text == '上映时间:':
                        movie_time = movie_tag.text.replace(' ','').replace('\n','').replace('上映时间:','')

            item['movie_title'] = movie_title
            item['movie_type'] = movie_type
            item['movie_time'] = movie_time
            
            items.append(item)

        return items
