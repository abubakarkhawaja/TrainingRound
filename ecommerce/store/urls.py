from django.conf.urls import url
from . import views

app_name = 'store'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<catagory>\w+(?:-\w+)+)/$', views.product_list, name='catagory')
]