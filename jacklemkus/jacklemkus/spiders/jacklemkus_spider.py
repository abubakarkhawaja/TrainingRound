from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import w3lib.url

class ProductPageParser:
    GENDERS = ['Mens', 'Womens', 'Kids']

    def parse(self, response) -> dict:
        ProductPageParser.response = response
        yield {}

    def retailer_sku(self):
        return ProductPageParser.response.css('.sku::text').get()

    def product_name(self):
        return ProductPageParser.response.css('.product-name h1::text').get()

    def url(self):
        return ProductPageParser.response.url

    def image_urls(self) -> list:
        return ProductPageParser.response.css('.span1 div a img::attr(src)').getall()

    def product_brand(self) -> str:
        raw_description = self.raw_description()
        product_brand = 'n/a'
        if 'Item Brand' not in raw_description:
            return product_brand
        brand_index = raw_description.index('Item Brand') + 1
        return raw_description[brand_index]

    def gender(self) -> str:
        description = self.raw_description()
        for gender in self.GENDERS:
            if gender in description:
                return gender.lower().rstrip('s')
        return 'unisex'

    def skus_content(self) -> list[dict]:
        skus = []
        for sku_s in  ProductPageParser.response.css('.list-size li '):            
            sku_content = {}
            sku_content['currency'] = 'ZAR'
            sku_content['out_of_stock'] = False if  ProductPageParser.response.css('#product_addtocart_form') else True
            sku_content['price'] = self.product_price()
            sku_content['sku_id'] = int(sku_s.css('button::attr(data-productid)').get())
            sku_content['size'] = sku_s.css('button::text').get().replace(" ","").strip('\n')
            skus.append(sku_content)
        return sku_content

    def raw_description(self) -> list:
        row = ProductPageParser.response.css('#product-attribute-specs-table > tbody > tr')
        column_lable = [cell.css('th::text').get() for cell in row]
        column_data = [cell.css('td::text').get() for cell in row]
        brand_description = ProductPageParser.response.css('.std::text').get()
        
        column_lable_and_data = self.append_column_lable_and_data(column_lable, column_data)
        column_lable_and_data.insert(0, brand_description)

        return column_lable_and_data

    def append_column_lable_and_data(self, column_label, column_data) -> list:
        column_size = len(column_label)
        description = []
        for i in range(column_size):
            description.append(column_label[i])
            description.append(column_data[i])
        return description

    def product_price(self) -> float:
        price = ProductPageParser.response.css('.price::text').re_first(r'R\s*(.*)')
        return float(price.replace(',', ''))

class ItemSpider(ProductPageParser, CrawlSpider):
    name = 'jacklemkus'
    allowed_domains = ['jacklemkus.com']
    start_urls = ['https://www.jacklemkus.com']
    listing_css = ['#nav > li.level0 > a.menu-link']
    products_css = ['#products-grid']

    rules = [
        Rule(LinkExtractor(restrict_css=listing_css), callback='parse_pagination'),
        Rule(LinkExtractor(restrict_css=products_css), callback='parse')
    ]

    def parse_pagination(self, response):
        last_page = self.response.css('div.js-infinite-scroll-pager-data::attr(data-lastpage)').get()
        
        if not last_page:
            return None
        for page_number in range(1, int(last_page)+1):
            url = w3lib.url.add_or_replace_parameter(response.url, 'p', page_number)
            yield response.follow(url, callback=self._parse)
