from django.shortcuts import render
from .models import Products

def index(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/index.html', context)