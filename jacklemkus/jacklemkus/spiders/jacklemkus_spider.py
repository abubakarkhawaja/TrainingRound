from scrapy.spiders import Spider, Rule
from scrapy.linkextractors import LinkExtractor

from product_page_parser import ProductPageParser


class ItemSpider(Spider):
    name = 'jacklemkus'
    allowed_domains = ['jacklemkus.com']
    start_urls = ['https://www.jacklemkus.com']
    rules = [
        Rule(LinkExtractor(),
        callback='parse_paginations')
    ]

    def parse_paginations(self, response):
        """
        Collects url of all products pages and follows them

        @params
        :response HtmlResponse: Response of HTML page

        @yield
        :dict: Dictionary of Product Information
        """
        product_urls = response.css('.product-name a::attr(href)').getall()
        for product_url in product_urls:
            yield response.follow(product_url, callback = self.parse_product_page)

    def parse_product_page(self, response):
        """
        Collects product information

        @params
        :response HtmlResponse: Response of HTML page

        @yield
        :dict: Dictionary of Product Information
        """
        product_page_parser = ProductPageParser(response)
        product_page_parser.set_product_info()
        yield product_page_parser.get_product_info()
