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

名称变化，修改部分代码。

4.运行爬虫，调试出现的问题

'''shell
cd ./maoyan/maoyan/spiders
scrapy crawl movie
'''

增加影片类型是否为空的判断，提升程序健壮性。
