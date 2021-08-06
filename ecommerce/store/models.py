from django.db import models


class Description(models.Model):
    retailer_sku = models.ForeignKey('Products', models.DO_NOTHING, db_column='retailer_sku', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description'

class ImageUrls(models.Model):
    retailer_sku = models.ForeignKey('Products', models.DO_NOTHING, db_column='retailer_sku', blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_urls'


class Products(models.Model):
    retailer = models.TextField(blank=True, null=True)
    spider_name = models.TextField(blank=True, null=True)
    retailer_sku = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    market = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    catergory = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    environment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Skus(models.Model):
    retailer_sku = models.ForeignKey(Products, models.DO_NOTHING, db_column='retailer_sku', blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    out_of_stock = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    sku_id = models.IntegerField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skus'
