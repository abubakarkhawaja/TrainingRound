class ProductPageParser:
    def __init__(self, response) -> None:
        """
        Constructor

        @params
        :response HtmlResponse: hold html response of product page
        """
        self.product_info = {}
        self.response = response

    def set_product_info(self) -> None:
        """
        Sets attributes of product information
        """
        self.description_content = self.get_description_content()
        self.gender = self.get_gender(self.description_content)
        self.product_brand = self.get_product_brand(self.description_content)
        self.skus_content = self.get_skus_content()

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
                'price': self.get_price_in_decimal(),
                'catagory': [
                    self.product_brand
                ],
                'image_urls': self.response.css('.span1 div a img::attr(src)').getall(),
                'brand': self.product_brand,
                'currency': 'ZAR',
                'environment': 'production',
        }

    def get_product_info(self) -> dict:
        """
        Returns product info

        @return
        :dict: Product Information as dictionary
        """
        return self.product_info

    def get_product_brand(self, description_content: list) -> str:
        """
        Returns product brand name from list

        @params
        :description_content list: list of table products

        @return
        :str: product brand name
        """
        product_brand = 'n/a'
        if 'product Brand' in description_content:
            brand_index =  description_content.index('product Brand') + 1
            product_brand = description_content[brand_index]
        return product_brand

    def get_gender(self, description_content: list) -> str:
        """
        Returns gender from list

        @params
        :description_content (list): list of table products]

        Returns:
        :str: Gender for product
        """
        gender = 'unisex'
        if 'Gender' in description_content:
            gender_index = description_content.index('Gender') + 1
            gender = description_content[gender_index]
            gender = gender.split(' ')[0]
            gender = gender.lower()
            if gender.endswith('s'):
                gender = gender[:-1]
        return gender

    def get_skus_content(self) -> list[dict]:
        """
        Returns skus content

        @return
        :list[dict]: List of dictionaries containting skus data
        """
        skus = []
        for sku in self.response.css('.list-size li '):
            skus.append({
                "currency": "ZAR",
                "out_of_stock": False if self.response.css('#product_addtocart_form') else True,
                "price": self.get_price_in_decimal(),
                "sku_id": int(sku.css('button::attr(data-productid)').get()),
                "size": sku.css('button::text').get().replace(" ","").strip('\n'),
            })
        return skus

    def get_description_content(self) -> list:
        """
        Returns table cell values in form of list

        @return
        :list: list of table values
        """
        row = self.response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr')
        column_lable = [cell.css('th::text').get() for cell in row]
        column_data = [cell.css('td::text').get() for cell in row]
        brand_description = self.response.css('.std::text').get()
        
        column_lable_and_data = self.append_column_lable_and_data(column_lable, column_data)
        column_lable_and_data.insert(0, brand_description)

        return column_lable_and_data

    def append_column_lable_and_data(self, column_label, column_data) -> list:
        """
        Combines two list small index first from both list first

        @params
        :column_label list: All column labels of table
        :column_data list: All data of labels of table

        @return
        :list: flattened list of column data and its lable
        """
        column_size = len(column_label)
        description = []
        for i in range(column_size):
            description.append(column_label[i])
            description.append(column_data[i])
        return description

    def get_price_in_decimal(self) -> float:
        """
        Converts price with currency tag to float

        @return
        :float: Numeric value of price
        """
        price = self.response.css('.price::text').get()
        price_without_tag = price.strip('R')
        price_without_tag = float(price_without_tag.replace(',', ''))
        return price_without_tag
