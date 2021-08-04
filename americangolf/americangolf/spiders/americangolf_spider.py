import w3lib.url

from scrapy.spiders import CrawlSpider, Rule
from scrapy.link import Link
from scrapy.linkextractors import LinkExtractor


class ProductPageParser:

    def parse_product_page(self, response):
        ProductPageParser.response = response
        product = {}
        yield product

    def retailer_sku(self):
        return ProductPageParser.response.css('div.product-code > div.product-number > span::text').get()

    def product_name(self):
        return ProductPageParser.response.css('h1.product-name ::text').get().strip('\n')

    def url(self):
        return ProductPageParser.response.url

    def image_urls(self) -> list:
        return ProductPageParser.response.css('ul.carousel > li.carousel-tile > a::attr(href)').getall()

    def product_brand(self) -> str:
        product_brand = ProductPageParser.response.css('div.product-brand img::attr(alt)').get()
        return product_brand

    def gender(self) -> str:
        gender = 'unisex'
        name = self.product_name()
        if 'Ladies' in name:
            gender = 'women'
        if 'Men' in name:
            gender = 'men'
        if 'Junior' in name:
            gender = 'kids'
        return gender

    def skus_content(self) -> list[dict]:
        skus = []
        sku_content = {}
        for sku in ProductPageParser.response.css('div.product-variations > ul > li > div.value > ul.swatches > li.swatch ch'):          
            sku_content['currency'] = 'EUR'
            sku_content['out_of_stock'] = True if str(ProductPageParser.response.css('div.out-of-stock::text').get()).strip() == 'Out of stock' else False
            sku_content['price'] = self.product_price()
            sku_content['sku_id'] = self.retailer_sku()
            sku_content['size'] = sku.css('li > a > span::text').get()
            skus.append(sku_content)

        for sku in ProductPageParser.response.css('#va-loft'):
            sku_content['currency'] = 'EUR'
            sku_content['out_of_stock'] = True if str(ProductPageParser.response.css('div.out-of-stock::text').get()).strip() == 'Out of stock' else False
            sku_content['price'] = self.product_price()
            sku_content['sku_id'] = self.retailer_sku()
            sku_content['size'] = sku.css('option::text').get().strip('\n').strip()
            if sku_content['size'] == 'Select Loft' or sku_content['size'].split()[0] == 'Adjustable':
                sku_content['size'] = 'N/a' 
            skus.append(sku_content)
        return skus

    def raw_description(self) -> list:
        description = []
        description.append(' '.join(paragraph.strip('\n') for paragraph in ProductPageParser.response.css('.product-detaildescription > div.paragraph::text').getall()))
        description.append(ProductPageParser.response.css('div.product-detaildescription > h4::text').get())
        for feature in ProductPageParser.response.css('ul.bullet-list > li'):
            description.append(feature.css('li::text').get())
        
        return description

    def product_price(self) -> float:
        price = ProductPageParser.response.css('div.product-sales-price::text').re_first(r'\s*(.*) €')
        if not price:
            price = ProductPageParser.response.css('div.product-sales-price span::text').re_first(r'\s*(.*) €')
        
        price = price.replace('.', '').replace(',','.')
        return float(price)

class AmericanGolfSpider(CrawlSpider, ProductPageParser):
    name = 'americangolf'
    allowed_domains = ['americangolf.eu']
    start_urls = ['https://www.americangolf.eu']
    header_css = ['#header-navigation']
    products_css = ['#search-result-items']
    
    rules = [
        Rule(LinkExtractor(restrict_css=header_css[0]), callback='parse'),
        Rule(LinkExtractor(restrict_css=products_css[0]), callback='parse_product_page', process_links='remove_variant')
    ]

    def remove_variant(self, links):
        for link in links:
            if '?' in link.url:
                yield Link(link.url.split('?')[0])
            else:
                yield link

    def parse(self, response):
        result_item_data = response.css('#search-result-items::attr(data-infinitescroll)').get()
        if not result_item_data:
            return
        
        result_item_data = eval(result_item_data)
        productCount = result_item_data['productCount']
        url = w3lib.url.add_or_replace_parameter(f'{response.url}?start=arg1&sz=arg2', 0, productCount)
        
        yield response.follow(url, callback=self._parse)
