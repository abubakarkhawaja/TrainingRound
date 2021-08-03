# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JacklemkusPipeline:
    def process_item(self, item, spider):
        item['retailer'] = 'jacklemkus'
        item['spider_name'] = 'jacklemkus'
        item['retailer-sku'] = spider.retailer_sku()
        item['name'] = spider.item_name()
        item['gender'] = spider.gender()
        item['url'] = spider.url()
        item['decription'] = spider.raw_description()
        item['market'] = 'ZA'
        item['skus'] = spider.skus_content()
        item['brand'] = spider.product_brand()
        item['price'] = spider.product_price()
        item['image_urls'] = spider.image_urls()
        item['catagory'] = [item['brand']]
        item['currency'] = item['skus'][0].get('currency')
        item['environment'] = 'production'
        return item
