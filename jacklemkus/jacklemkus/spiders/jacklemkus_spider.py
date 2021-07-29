from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ItemSpider(CrawlSpider):
    name = 'jacklemkus'
    allowed_domains = ['jacklemkus.com']
    start_urls = ['https://www.jacklemkus.com']

    rules = [
        Rule(LinkExtractor(allow=r'^https://www.jacklemkus.com/(\w+$|(\w+-\w+$))', restrict_css='#nav'), callback='parse_pagination'),
        Rule(LinkExtractor(restrict_css='#products-grid'), callback='parse')
    ]

    def parse_pagination(self, response):
        last_page = response.css("div.js-infinite-scroll-pager-data::attr(data-lastpage)").get()
        if last_page:
            for page_number in range(1, int(last_page)+1):
                url = response.url + f"?p={page_number}"
                yield response.follow(url, callback=self._parse)

    def parse(self, response) -> dict:
        product_parser = ProductPageParser()
        product = {}
        product['retailer'] = 'jacklemkus'
        product['spider_name'] = "jacklemkus"
        product['retailer-sku'] = product_parser.retailer_sku(response)
        product['name'] = product_parser.product_name(response)
        product['gender'] = product_parser.gender(product_parser.raw_description(response))
        product['url'] = response.url
        product['decription'] = product_parser.raw_description(response)
        product['market'] = 'ZA'
        product['skus'] = product_parser.skus_content(response)
        product['price'] = product_parser.product_price(response)
        product['catagory'] = [product_parser.product_brand(product_parser.raw_description(response))]
        product['image_urls'] = product_parser.image_urls(response)
        product['brand'] = product_parser.product_brand(product_parser.raw_description(response))
        product['currency'] = 'ZAR'
        product['environment'] = 'production'
        yield product

class ProductPageParser:
    def retailer_sku(self, response):
        return response.css('.sku::text').get()

    def product_name(self, response):
        return response.css('.product-name h1::text').get()

    def image_urls(self, response) -> list:
        return response.css('.span1 div a img::attr(src)').getall()

    def product_brand(self, raw_description: list) -> str:
        product_brand = 'n/a'
        if 'Item Brand' in raw_description:
            brand_index = raw_description.index('Item Brand') + 1
            product_brand = raw_description[brand_index]
        return product_brand

    def gender(self, raw_description: list) -> str:
        gender = 'unisex'
        if 'Gender' in raw_description:
            gender_index = raw_description.index('Gender') + 1
            gender = raw_description[gender_index]
            gender = gender.split(' ')[0].lower()
            if gender.endswith('s'):
                gender = gender[:-1]
        return gender

    def skus_content(self, response) -> list[dict]:
        skus = []
        for sku in  response.css('.list-size li '):            
            skus.append(self.parse_sku(response, sku))
        return skus

    def parse_sku(self, response, sku):
        sku_content = {}
        sku_content["currency"] = "ZAR"
        sku_content["out_of_stock"] = False if  response.css('#product_addtocart_form') else True
        sku_content["price"] = self.product_price(response)
        sku_content["sku_id"] = int(sku.css('button::attr(data-productid)').get())
        sku_content["size"] = sku.css('button::text').get().replace(" ","").strip('\n')
        return sku_content

    def raw_description(self, response) -> list:
        row = response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr')
        column_lable = [cell.css('th::text').get() for cell in row]
        column_data = [cell.css('td::text').get() for cell in row]
        brand_description = response.css('.std::text').get()
        
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

    def product_price(self, response) -> float:
        price = response.css('.price::text').re_first(r'R\s*(.*)')
        return float(price.replace(',', ''))
