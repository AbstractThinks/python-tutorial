# -*- coding:utf-8 -*-
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.spiders.BaseSpider):
    name = "dmoz2"

    allowed_domains = ["domz.org"]
    start_urls = [
        "http://www.domz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.domz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    # allowed_domain = ["baidu.com"]
    # start_urls = [
    #     'http://www.baidu.com'
    # ]


    def parse(self, response):
        # hxs = scrapy.selector.HtmlXPathSelector(response)
        # sites = hxs.select('//ul/li')   #//ul/li  选择所有ul标签下的li标签

        # sites = hxs.select('//a')
        # items = []
        # for site in sites:
            # title = site.select('a/text()').extract()    #选择a标签文本
            # link = hxs.select('/@href').extract()
            # link = site.select('a/@href').extract()      #a/@href 选择所有a标签的href属性 a[@href="abc"]选择所有href属性为'abc'的a标签
            # desc = site.select('text()').extract()

        item = DmozItem()
            # item['title'] = title
            # item['link'] = link
            # item['desc'] = desc

            # items.append(item)

        # return items
        href = response.xpath('//a/@href').extract()
        item['movie_href'] = href
        return item
            # print("title: " + title)
            # print("link: " + link)
            # print("desc: " + desc)