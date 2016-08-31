# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from tutorial.items import MovieItem



class DoubanSpider(BaseSpider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "https://movie.douban.com/subject_search?search_text=action&cat=1002"
    ]

    def start_requests(self):
        yield Request("https://movie.douban.com/subject_search?search_text=action&cat=1002", headers={
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"})

    def parse(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//tr[@class="item"]/td/a[@class="nbg"]')
        items = []

        for site in sites:
            movie_description = site.xpath('@href').extract()
            # movie_description = site.extract()
            item = MovieItem()
            item['movie_description'] = movie_description
            items.append(item)
        return items


# 启动命令scrapy crawl douban -o items.json -t json