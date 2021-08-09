from django.shortcuts import render
from .models import ImageUrls, Products

def index(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/index.html', context)
    
def product_list(request, catagory):
    products = Products.objects.filter(catergory=catagory)
    
    # image_urls = ImageUrls.objects.all()
    
    # for image_url in image_urls:
    #     print(image_url.url)

    context = {
        'products': products,
        # 'image_urls': image_urls,
        'catagory': ''.join(catagory.split('-')).title()
    }
    return render(request, 'store/product_list.html', context)