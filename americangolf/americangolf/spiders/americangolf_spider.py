from scrapy.spiders import CrawlSpider, Rule
from scrapy.link import Link
from scrapy.linkextractors import LinkExtractor


class ProductPageParser:
    def parse_product_page(self, response):
        product = {}
        product['retailer'] = 'jacklemkus'
        product['spider_name'] = 'jacklemkus'
        product['retailer-sku'] = self.retailer_sku(response)
        product['name'] = self.product_name(response)
        product['gender'] = self.gender(response)
        product['url'] = response.url
        product['description'] = self.raw_description(response)
        product['market'] = 'EU'
        product['skus'] = self.skus_content(response)
        product['price'] = self.product_price(response)
        product['catagory'] = [self.product_brand(response)]
        product['image_urls'] = self.image_urls(response)
        product['brand'] = self.product_brand(response)
        product['currency'] = 'EUR'
        product['environment'] = 'production'
        yield product

    def retailer_sku(self, response):
        return response.css('div.product-code > div.product-number > span::text').get()

    def product_name(self, response):
        return response.css('h1.product-name ::text').get().strip('\n')

    def image_urls(self, response) -> list:
        return response.css('ul.carousel > li.carousel-tile > a::attr(href)').getall()

    def product_brand(self, response: list) -> str:
        product_brand = response.css('div.product-brand img::attr(alt)').get()
        return product_brand

    def gender(self, response) -> str:
        gender = 'unisex'
        name = self.product_name(response)
        if 'Ladies' in name:
            gender = 'women'
        if 'Men' in name:
            gender = 'men'
        if 'Junior' in name:
            gender = 'kids'
        return gender

    def skus_content(self, response) -> list[dict]:
        skus = []
        sku_content = {}
        for sku in response.xpath('//*[@id="product-content"]/div/div[1]/ul/li[2]/div[2]/ul/li'):            
            sku_content['currency'] = 'EUR'
            sku_content['out_of_stock'] = False if response.css('button#add-to-cart') else True
            sku_content['price'] = self.product_price(response)
            sku_content['sku_id'] = self.retailer_sku(response)
            sku_content['size'] = sku.css('li > a > span::text').get()
            skus.append(sku_content)

        for sku in response.css('#va-loft option'):
            sku_content['currency'] = 'EUR'
            sku_content['out_of_stock'] = False if response.css('button#add-to-cart') else True
            sku_content['price'] = self.product_price(response)
            sku_content['sku_id'] = self.retailer_sku(response)
            sku_content['size'] = sku.css('option::text').get().strip('\n')
            if sku_content['size'] != 'Select Loft':
                skus.append(sku_content)
        return skus

    def raw_description(self, response) -> list:
        description = []
        description.append(' '.join(paragraph.strip('\n') for paragraph in response.css('.product-detaildescription > div.paragraph::text').getall()))
        description.append(response.xpath('//*[@id="anchor-product-details"]/div/div/div[2]/h4/text()').get())
        for feature in response.css('ul.bullet-list > li'):
            description.append(feature.css('li::text').get())
        
        return description

    def product_price(self, response) -> float:
        price = response.css('div.product-sales-price::text').re_first(r'\s*(.*) €')
        if not price:
            price = response.css('div.product-sales-price span::text').re_first(r'\s*(.*) €')
        if ',' in price:
            price = price.split('.')[0].replace(',', '.')
        return float(price)

class AmericanGolfSpider(CrawlSpider, ProductPageParser):
    name = 'americangolf'
    allowed_domains = ['americangolf.eu']
    start_urls = ['https://www.americangolf.eu']
    header_css ='#header-navigation'
    products_css = '#search-result-items'
    
    rules = [
        Rule(LinkExtractor(restrict_css=header_css), callback='parse'),
        Rule(LinkExtractor(restrict_css=products_css), callback='parse_product_page', process_links='remove_variant')
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
        yield response.follow(f'{response.url}?start=0&sz={productCount}', callback=self._parse)
