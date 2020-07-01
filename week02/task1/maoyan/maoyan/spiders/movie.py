import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']

    def start_requests(self):

        for i in range(0, 10):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):

        items = []

        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')

        for movie in movies:

            item = MaoyanItem()
            
            # 电影名称获取
            movie_title = movie.xpath('./div/span/text()').extract_first()
            item['movie_title'] = movie_title

            #电影类型获取
            movie_info_list = movie.xpath('./div[@class="movie-hover-title"]/text()').extract()
            movie_info_list_new = []

            for x in movie_info_list:
                x = x.replace('\n','').replace(' ','')
                if x != '':
                    movie_info_list_new.append(x)

            #存在电影类型为空的情况
            if movie_info_list_new == []:
                item['movie_type'] = '暂无'
            else:
                movie_type = movie_info_list_new[0]
                item['movie_type'] = movie_type

            #电影上映时间获取
            movie_time_list = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()').extract()
            movie_time_list_new = []

            for y in movie_time_list:
                y = y.replace('\n','').replace(' ','')
                if y != '':
                    movie_time_list_new.append(y)

            #存在电影上映时间为空的情况
            movie_time = ''.join(movie_time_list_new)
            if movie_time == '':
                movie_time = '暂无'

            item['movie_time'] = movie_time

            items.append(item)

        return items
