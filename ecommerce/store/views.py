from django.shortcuts import render

from .models import Products


def index(request):
    products = Products.objects.all()
    context = {"products": products}
    return render(request, "store/index.html", context)


def product_list(request, catagory: str):
    products = Products.objects.filter(catergory=catagory)

    context = {"products": products, "catagory": "".join(catagory.split("-")).title()}
    return render(request, "store/product_list.html", context)


def details(request, pk: int):
    product = Products.objects.get(pk=pk)
    return render(request, "store/details.html", {"product": product})
