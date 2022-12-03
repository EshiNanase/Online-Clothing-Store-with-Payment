from django.shortcuts import render, HttpResponse
from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'products/index.html', context)


def store(request):
    context = {'title': 'Store - Каталог',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()
               }
    return render(request, 'products/products.html', context)