from unittest import  mock, TestCase

from jacklemkus.spiders.jacklemkus_spider import ProductPageParser


class TestSpider(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.product_parser = ProductPageParser(mock.Mock)
        cls.patcher = mock.patch('spiders.product_page_parser.ProductPageParser.fetch_product_info', return_value={'name': 'dummy'})
        cls.patcher.start()

    def test_fetch_product_info(self) -> None:
        self.assertIsNotNone(self.product_parser.fetch_product_info())
    
    def test_gender(self) -> None:
        self.assertEqual(self.product_parser.gender([]), 'unisex')

    def test_append_column_lable_and_data(self) -> None:
        appended_column = self.product_parser.append_column_lable_and_data(['lable1','lable2'], ['data1', 'data2'])
        self.assertEqual(appended_column, ['lable1', 'data1', 'lable2', 'data2'])

    @mock.patch('spiders.product_page_parser.ProductPageParser.get_price_in_decimal', return_value=1998.0)
    def test_price_in_decimal(self, mock_get_price_in_decimal) -> None:
        self.assertIsInstance(self.product_parser.price_in_decimal(), float) 

    @classmethod
    def tearDownClass(cls) -> None:
        cls.patcher.stop()
