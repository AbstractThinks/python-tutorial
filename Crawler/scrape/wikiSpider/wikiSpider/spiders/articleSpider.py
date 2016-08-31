# -*- coding:utf-8 -*-

from scrapy.selector import Selector
from scrapy import Spider, Request
from wikiSpider.spiders.items import Article

# 启动命令

# scrapy crawl article -o item.json -t json
class ArticleSpider(Spider):
    name = "article"
    # allow_domains = ["en.wikipedia.org"]
    # start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
    #         "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    # start_urls = [
    #     "http://en.wikipedia.org/wiki/Main_Page"
    # ]

    allow_domains = ["movie.douban.com"]
    start_urls = [
        "https://movie.douban.com/subject_search?search_text=action&cat=1002"
    ]
    # 防爬虫网站需要添加
    def start_requests(self):
        yield Request("https://movie.douban.com/subject_search?search_text=action&cat=1002",headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"})

    def parse(self, response):
        # http://en.wikipedia.org/wiki/Main_Page
        # item = Article()
        # title = response.xpath('//h1/text()')[0].extract()
        # item['title'] = title
        # return item

        # http://en.wikipedia.org/wiki/Main_Page
        # items = []
        # sites = response.xpath('//ul/li/a/@href').extract()
        # for site in sites:
        #     item = Article()
        #     item['title'] = site
        #     items.append(item)
        #
        # return items

        # http://en.wikipedia.org/wiki/Main_Page
        items = []
        sites = response.xpath('//tr[@class="item"]/td/a[@class="nbg"]/@href').extract()
        for site in sites:
            item = Article()
            item['title'] = site
            items.append(item)

        return items



