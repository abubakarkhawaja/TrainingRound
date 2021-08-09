from .models import Description, ImageUrls, Products, Skus
from django.contrib import admin

# Register your models here.
admin.site.register(Products)
admin.site.register(Skus)
admin.site.register(Description)
admin.site.register(ImageUrls)
