 # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from mysql import connector
import json

TABLE_NAME = "products"
DESC_TABLE = "description"
SKUS_TABLE = "skus"
URL_TABLE = "image_urls"

class AmericangolfPipeline:
    def __init__(self) -> None:
        self.create_connection()
        self.create_table()
    
    def create_connection(self) -> None:
        self.connection = connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'rootison',
            database = 'americangolf'
        )
        self.current_cursor = self.connection.cursor()

    def create_table(self) -> None:
        self.current_cursor.execute(f"""DROP TABLE IF EXISTS {DESC_TABLE}""")
        self.current_cursor.execute(f"""DROP TABLE IF EXISTS {SKUS_TABLE}""")
        self.current_cursor.execute(f"""DROP TABLE IF EXISTS {URL_TABLE}""")
        self.current_cursor.execute(f"""DROP TABLE IF EXISTS {TABLE_NAME}""")
        
        self.current_cursor.execute(f"""
        create table {TABLE_NAME}(
            retailer text, spider_name text, retailer_sku int PRIMARY KEY, name text, gender text, url text, market text, 
            price float, catergory text, brand text, currency text, environment text )
        """)
        self.current_cursor.execute(f"""
        create table {DESC_TABLE}(
            retailer_sku int, FOREIGN KEY(retailer_sku) REFERENCES {TABLE_NAME}(retailer_sku), description text)
        """)
        self.current_cursor.execute(f"""
        create table {SKUS_TABLE}(
            retailer_sku int, FOREIGN KEY(retailer_sku) REFERENCES {TABLE_NAME}(retailer_sku), currency text, out_of_stock bool, price float, sku_id int, size text)
        """)
        self.current_cursor.execute(f"""
        create table {URL_TABLE}(
            retailer_sku int, FOREIGN KEY(retailer_sku) REFERENCES {TABLE_NAME}(retailer_sku), image_url text)
        """)

    def process_item(self, item, spider):
        item['retailer'] = 'americangolf'
        item['spider_name'] = 'americangolf'
        item['retailer-sku'] = spider.retailer_sku()
        item['name'] = spider.product_name()
        item['gender'] = spider.gender()
        item['url'] = spider.url()
        item['description'] = spider.raw_description()
        item['market'] = 'EUR'
        item['skus'] = spider.skus_content()
        item['brand'] = spider.product_brand()
        item['price'] = spider.product_price()
        item['image_urls'] = spider.image_urls()
        item['catagory'] = [item['brand']]
        item['currency'] = 'EUR'
        item['environment'] = 'production'

        self.store(item)
        return item
    
    def store(self, item):
        self.current_cursor.execute(f"""
            insert into {TABLE_NAME} 
            values (
                '{item['retailer']}', '{item['spider_name']}', '{item['retailer-sku']}', '{item['name']}', '{item['gender']}', '{item['url']}', 
                '{item['market']}', '{item['price']}', '{item['catagory'][0]}', '{item['brand']}', '{item['currency']}', '{item['environment']}')
            """)

        for raw_description in item['description']:
            if raw_description:
                description = str(raw_description).replace("'", "\\'")
                self.current_cursor.execute(f"""insert into {DESC_TABLE} values ('{item['retailer-sku']}', '{description}')""")
        
        for sku in item['skus']:
            self.current_cursor.execute(f"""insert into {SKUS_TABLE} values ('{item['retailer-sku']}', '{sku['currency']}', '{int(sku['out_of_stock'])}', 
                '{sku['price']}', '{sku['sku_id']}', '{sku['size']}')""")
        
        for image_url in item['image_urls']:
            self.current_cursor.execute(f"""insert into {URL_TABLE} values ('{item['retailer-sku']}', '{image_url}')""")

        self.connection.commit()
