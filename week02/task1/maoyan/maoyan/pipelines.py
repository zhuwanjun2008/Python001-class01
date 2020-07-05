# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pymysql

class MaoyanPipeline:
    def process_item(self, item, spider):

        movie_title =  item['movie_title']
        movie_type =  item['movie_type']
        movie_time = item['movie_time']

        #output = [f'名称:{movie_title},类型: {movie_type},上映时间: {movie_time}']
        #movie_pd = pd.DataFrame(data = output)
        #movie_pd.to_csv('./movie.csv', mode='a', encoding='utf8', index=False, header=False)

        #数据保存方式，调整为mysql
        conn = pymysql.connect(
            host = 'localhost', 
            port = 3306, 
            user = 'maoyan', 
            password = '1qaz@WSX', 
            db = 'maoyan')

        cur = conn.cursor()

        #符合SQL语法，语句中增加双引号
        sql = f'INSERT INTO movie VALUES ("{movie_title}","{movie_type}","{movie_time}")'

        try:
            cur.execute(sql)
            conn.commit()
        except (Exception) as e:
            print(e)
            conn.rollback()
        
        conn.close()

        return item
