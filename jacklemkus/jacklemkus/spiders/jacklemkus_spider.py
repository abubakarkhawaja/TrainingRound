from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ItemSpider(CrawlSpider):
    name = 'jacklemkus'
    allowed_domains = ['jacklemkus.com']
    start_urls = ['https://www.jacklemkus.com']

    rules = [
        Rule(LinkExtractor(restrict_xpaths='//*[@id="nav"]'), callback='parse'),
        Rule(LinkExtractor(restrict_xpaths='//*[@id="products-grid"]'), callback='parse_product_page')
    ]

    def parse(self, response):
        last_page = response.css("div.js-infinite-scroll-pager-data::attr(data-lastpage)").get()
        if last_page:
            for page_number in range(1, int(last_page)+1):
                url = response.url + f"?p={page_number}"
                yield response.follow(url, callback=self._parse)

    def parse_product_page(self, response):
        product_page_parser = ProductPageParser(response)
        product_page_parser.fetch_product_info()
        yield product_page_parser.product_info

class ProductPageParser:
    def __init__(self, response) -> None:
        self.product_info = {}
        self.response = response

    def fetch_product_info(self) -> None:
        self.description_content = self.description_content()
        self.gender = self.gender(self.description_content)
        self.product_brand = self.product_brand(self.description_content)
        self.skus_content = self.skus_content()

        self.product_info = {
                'retailer': 'jacklemkus',
                'spider_name': "jacklemkus",
                'retailer-sku': self.response.css('.sku::text').get(),
                'name': self.response.css('.product-name h1::text').get(),
                'gender': self.gender,
                'url': self.response.url,
                'decription': self.description_content,
                'market': 'ZA',
                'skus': self.skus_content,
                'price': self.price_in_decimal(),
                'catagory': [
                    self.product_brand
                ],
                'image_urls': self.response.css('.span1 div a img::attr(src)').getall(),
                'brand': self.product_brand,
                'currency': 'ZAR',
                'environment': 'production',
        }

    def product_brand(self, description_content: list) -> str:
        product_brand = 'n/a'
        if 'product Brand' in description_content:
            brand_index =  description_content.index('product Brand') + 1
            product_brand = description_content[brand_index]
        return product_brand

    def gender(self, description_content: list) -> str:
        gender = 'unisex'
        if 'Gender' in description_content:
            gender_index = description_content.index('Gender') + 1
            gender = description_content[gender_index]
            gender = gender.split(' ')[0]
            gender = gender.lower()
            if gender.endswith('s'):
                gender = gender[:-1]
        return gender

    def skus_content(self) -> list[dict]:
        skus = []
        for sku in self.response.css('.list-size li '):
            skus.append({
                "currency": "ZAR",
                "out_of_stock": False if self.response.css('#product_addtocart_form') else True,
                "price": self.price_in_decimal(),
                "sku_id": int(sku.css('button::attr(data-productid)').get()),
                "size": sku.css('button::text').get().replace(" ","").strip('\n'),
            })
        return skus

    def description_content(self) -> list:
        row = self.response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr')
        column_lable = [cell.css('th::text').get() for cell in row]
        column_data = [cell.css('td::text').get() for cell in row]
        brand_description = self.response.css('.std::text').get()
        
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

    def price_in_decimal(self) -> float:
        price = str(self.response.css('.price::text').get())
        price_without_tag = price.strip('R')
        price_without_tag = float(price_without_tag.replace(',', ''))
        return price_without_tag
