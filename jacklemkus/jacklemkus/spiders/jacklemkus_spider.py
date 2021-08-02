from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ProductPageParser:
    def parse(self, response) -> dict:
        product = {}
        product['retailer'] = 'jacklemkus'
        product['spider_name'] = 'jacklemkus'
        product['retailer-sku'] = self.retailer_sku(response)
        product['name'] = self.product_name(response)
        product['gender'] = self.gender(self.raw_description(response))
        product['url'] = response.url
        product['decription'] = self.raw_description(response)
        product['market'] = 'ZA'
        product['skus'] = self.skus_content(response)
        product['price'] = self.product_price(response)
        product['catagory'] = [self.product_brand(self.raw_description(response))]
        product['image_urls'] = self.image_urls(response)
        product['brand'] = self.product_brand(self.raw_description(response))
        product['currency'] = 'ZAR'
        product['environment'] = 'production'
        yield product

    def retailer_sku(self, response):
        return response.css('.sku::text').get()

    def product_name(self, response):
        return response.css('.product-name h1::text').get()

    def image_urls(self, response) -> list:
        return response.css('.span1 div a img::attr(src)').getall()

    def product_brand(self, raw_description: list) -> str:
        product_brand = 'n/a'
        if 'Item Brand' not in raw_description:
            return product_brand
        brand_index = raw_description.index('Item Brand') + 1
        product_brand = raw_description[brand_index]
        return product_brand

    def gender(self, raw_description: list) -> str:
        gender = 'unisex'
        if 'Gender' not in raw_description:
            return gender
        gender_index = raw_description.index('Gender') + 1
        gender = raw_description[gender_index]
        gender = gender.split(' ')[0].lower()
        if gender.endswith('s'):
            gender = gender[:-1]
        return gender

    def skus_content(self, response) -> list[dict]:
        skus = []
        for sku in  response.css('.list-size li '):            
            sku_content = {}
            sku_content['currency'] = 'ZAR'
            sku_content['out_of_stock'] = False if  response.css('#product_addtocart_form') else True
            sku_content['price'] = self.product_price(response)
            sku_content['sku_id'] = int(sku.css('button::attr(data-productid)').get())
            sku_content['size'] = sku.css('button::text').get().replace(" ","").strip('\n')
            skus.append(sku_content)
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

class ItemSpider(ProductPageParser, CrawlSpider):
    name = 'jacklemkus'
    allowed_domains = ['jacklemkus.com']
    start_urls = ['https://www.jacklemkus.com']
    listing_css = '#nav'
    products_css = '#products-grid'
    single_depth_url = r'^https://www.jacklemkus.com/(\w+$|(\w+-\w+$))'

    rules = [
        Rule(LinkExtractor(allow=single_depth_url, restrict_css=listing_css), callback='parse_pagination'),
        Rule(LinkExtractor(restrict_css=products_css), callback='parse')
    ]

    def parse_pagination(self, response):
        last_page = response.css('div.js-infinite-scroll-pager-data::attr(data-lastpage)').get()
        if not last_page:
            return None
        for page_number in range(1, int(last_page)+1):
            url = response.urljoin(f'?p={page_number}')
            yield response.follow(url, callback=self._parse)
