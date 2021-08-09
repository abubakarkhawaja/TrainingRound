# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
