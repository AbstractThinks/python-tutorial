# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from tutorial.items import MovieItem



class DoubanSpider(BaseSpider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "https://movie.douban.com/subject_search?search_text=action&cat=1002"
    ]


    def parse(self, response):
        # hxs = HtmlXPathSelector(response)
        # print(hxs)
        # sites = hxs.select('//td')
        # items = []

        # for site in sites:
        #     movie_description = site.select("a/text()").extract()
        #
        #     item = MovieItem()
        #     item['movie_description'] = movie_description
        #     items.append(item)
        # return items
        item = MovieItem()
        href = response.xpath('//a/@href').extract()
        item['movie_href'] = href
        return item

# 启动命令scrapy crawl douban -o items.json -t json