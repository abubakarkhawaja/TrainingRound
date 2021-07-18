import scrapy

from jacklemkus.spiders.product_page_parser import ProductPageParser


class ItemSpider(scrapy.Spider):
    name = 'jacklemkus'
    start_urls = ['https://www.jacklemkus.com']

    def parse(self, response):
        """
        Collects links of all catagories from menu bar

        @params
        :response HtmlResponse: Response of HTML page

        @yield
        :dict: Dictionary of Product Information
        """
        menu_items = response.xpath(f'//*[@id="nav"]/li')
        for menu_item in menu_items:
            menu_page_url = menu_item.css('a::attr(href)').get()
            yield response.follow(menu_page_url, callback= self.parse_menu_page)

    def parse_menu_page(self, response):
        """
        Collects url of all paginations within a page and follows them

        @params
        :response HtmlResponse: Response of HTML page

        @yield
        :dict: Dictionary of Product Information
        """
        products_pagination_urls = set(response.css('ol.pagination.left li a::attr(href)').getall())
        products_pagination_urls.add(response.url)
        for pagination_url in products_pagination_urls:
            yield response.follow(pagination_url, callback= self.parse_paginations) 

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
        yield product_page_parser.get_product_info()
