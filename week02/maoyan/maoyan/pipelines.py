# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class MaoyanPipeline:
    def process_item(self, item, spider):

        movie_title =  item['movie_title']
        movie_type =  item['movie_type']
        movie_time = item['movie_time']

        output = [f'名称:{movie_title},类型: {movie_type},上映时间: {movie_time}']

        movie_pd = pd.DataFrame(data = output)
        movie_pd.to_csv('./movie.csv', mode='a', encoding='utf8', index=False, header=False)

        return item
