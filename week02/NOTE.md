# 学习笔记

## 任务1

### Scrapy操作回顾

- 创建名为maoyan的项目

- 创建名为movie的爬虫

- 从week01项目，迁移功能代码
  - 名称变化，修改部分代码

- 运行爬虫，调试出现的问题
  - 增加影片类型是否为空的判断，提升程序健壮性

### 结果保存至数据库

- 安装mysql数据库

- 创建数据库、配置访问权限、创建数据表

- 修改pipeline，将爬虫书记写入movie表
  - insert语句要注意语法，字符串要增加单引号

### 访问增加代理

- 修改settings.py，开启中间件配置

- 编写中间件代理，主要来源自老师的示例

- 寻找可用的代理花了一些时间，后续考虑实现时使用商用服务

## 任务2

### requests还是selenium

- 原本打算使用requests，使用chrome浏览器未能抓取到网页登录请求，切换为selenium

- 安装chromedriver，注意选择版本
  - chrome版本为83.0.4103.116，选择chromedriver版本为83.0.4103.39
  - 下载文件解压后，移动到/usr/bin目录下（Linux）

- 根据xpath匹配案件和输入框的位置，顺利完成页面调转和信息输入
