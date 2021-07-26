from unittest import  mock, TestCase

from spiders.product_page_parser import ProductPageParser


class TestSpider(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        "Setups mocks and class objects which needed to initialize once"
        cls.product_parser = ProductPageParser(mock.Mock)
        cls.patcher = mock.patch('spiders.product_page_parser.ProductPageParser.get_product_info', return_value={
                "retailer": "jacklemkus", "spider_name": "dummy", "retailer-sku": "BV3634-410", "name": "Nike Boys Nsw Core Bf Trk Suit", 
                "gender": "boy", "url": "https://www.dummy.com/", 
                "decription": ["Nike Boys Nsw Core Bf Trk Suit", "Gender", "Boys Apparel", "Item Brand", "Nike", "Clothing Type", "Tracksuits"], 
                "market": "PKR", "skus": [
                    {"currency": "PKR", "out_of_stock": False, "price": 859.0, "sku_id": 171262, "size": "6-8"}, 
                    {"currency": "ZAR", "out_of_stock": True, "price": 859.0, "sku_id": 171262, "size": "8-10"},
                ], 
                "price": 859.0, "catagory": ["n/a"], "image_urls": [], "brand": "n/a", "currency": "PKR", "environment": "production"},
        
        )
        cls.patcher.start()

    def test_get_product_info(self) -> None:
        "Test for method if it returns None."
        self.assertIsNotNone(self.product_parser.get_product_info())
    
    def test_get_gender(self) -> None:
        "Test for method if it gender is correctly returned."
        self.assertEqual(self.product_parser.get_gender([]), 'unisex')

    def test_append_column_lable_and_data(self) -> None:
        "Test for method if it returns both correcftly combined list."
        appended_column = self.product_parser.append_column_lable_and_data(['lable1','lable2'], ['data1', 'data2'])
        self.assertEqual(appended_column, ['lable1', 'data1', 'lable2', 'data2'])

    @mock.patch('spiders.product_page_parser.ProductPageParser.get_price_in_decimal', return_value=1998.0)
    def test_get_price_in_decimal(self, mock_get_price_in_decimal) -> None:
        "Test for method if it returns float."
        self.assertIsInstance(self.product_parser.get_price_in_decimal(), float) 

    @classmethod
    def tearDownClass(cls) -> None:
        """Stopping all connections at end"""
        cls.patcher.stop()
