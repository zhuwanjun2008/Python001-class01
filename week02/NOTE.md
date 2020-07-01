# 学习笔记

## 回顾Scrapy操作

1.创建名为maoyan的项目

```shell
scrapy startproject maoyan
```

2.创建名为movie的爬虫

```shell
cd maoyan
scrapy genspider movie maoyan.com
```

3.从week01项目，迁移功能代码

项目和爬虫名称变化，修改部分代码

4.运行爬虫，调试出现的问题

'''shell
cd ./maoyan/maoyan/spiders
scrapy crawl movie
'''
