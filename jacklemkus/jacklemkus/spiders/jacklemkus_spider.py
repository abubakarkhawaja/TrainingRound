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
        yield product_page_parser.parse()

class ProductPageParser:
    def __init__(self, response) -> None:
        self.response = response

    def parse(self) -> dict:
        product_info = {}
        product_info['retailer'] = 'jacklemkus'
        product_info['spider_name'] = "jacklemkus"
        product_info['retailer-sku'] = self.response.css('.sku::text').get()
        product_info['name'] = self.response.css('.product-name h1::text').get()
        product_info['gender'] = self.gender(self.description_content())
        product_info['url'] = self.response.url
        product_info['decription'] = self.description_content()
        product_info['market'] = 'ZA'
        product_info['skus'] = self.skus_content()
        product_info['price'] = self.price_in_decimal()
        product_info['catagory'] = [self.product_brand(self.description_content())]
        product_info['image_urls'] = self.response.css('.span1 div a img::attr(src)').getall()
        product_info['brand'] = self.product_brand(self.description_content())
        product_info['currency'] = 'ZAR'
        product_info['environment'] = 'production'
        return product_info

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
            gender = gender.split(' ')[0].lower()
            if gender.endswith('s'):
                gender = gender[:-1]
        return gender

    def skus_content(self) -> list[dict]:
        skus = []
        for sku in self.response.css('.list-size li '):            
            skus.append(self.parse_sku(sku))
        return skus

    def parse_sku(self, sku):
        sku_content = {}
        sku_content["currency"] = "ZAR"
        sku_content["out_of_stock"] = False if self.response.css('#product_addtocart_form') else True
        sku_content["price"] = self.price_in_decimal()
        sku_content["sku_id"] = int(sku.css('button::attr(data-productid)').get())
        sku_content["size"] = sku.css('button::text').get().replace(" ","").strip('\n')
        return sku_content

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
        price = self.response.css('.price::text').re_first(r'R\s*(.*)')
        return float(price.replace(',', ''))
