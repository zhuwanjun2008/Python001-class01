# -*- coding: utf-8 -*-
import scrapy
from spider.items import SpiderItem
from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):

        for i in range(0, 2):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):

        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')

        for movie in movies:
            
            movie_title = movie.xpath('./div/span/text()').extract_first()

            movie_info = movie.xpath('./div/text()').extract()
            #print(movie_info)
            movie_type = movie_info[4].strip()
            movie_time = movie_info[8].strip()

            print(movie_title)
            print(movie_type)
            print(movie_time)
