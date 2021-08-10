from django.contrib import admin

from .models import Description, Images, Products, Skus

admin.site.register(Products)
admin.site.register(Skus)
admin.site.register(Description)
admin.site.register(Images)
