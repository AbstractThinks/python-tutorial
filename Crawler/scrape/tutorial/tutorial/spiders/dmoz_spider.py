# -*- coding:utf-8 -*-
import scrapy
class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = "dmoz.org"
    start_urls = [
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
            ]
    
    # 生成Books文件并将爬出来的数据写入
    def parse(self, response):
       filename = response.url.split("/")[-2]
       open(filename, "wb").write(response.body)
    

