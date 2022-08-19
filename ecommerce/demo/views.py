from cgitb import reset
from pydoc import pager
from django.core.paginator import Paginator
from urllib import request
from django.shortcuts import render
from ecommerce.inventory import models
from django.db.models import Count

def home(request):
    return render(request, 'base.html')

def category(request):
    data = models.Category.objects.annotate(Count('product')).order_by('-product__count')
    p = Paginator(data, 10)
    
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    num_categories = models.Category.objects.count()

    return render(request, 'categories.html', {"page_obj":page_obj, "num_category":num_categories})

def products_by_category(request, category):

    data = models.Product.objects.filter(category__name=category).values("id", "name", "slug", "description", "category__name", "product__store_price")
    p = Paginator(data, 42)

    pager_number = request.GET.get('page')
    page_obj = p.get_page(pager_number)
    
    num_products = models.Product.objects.filter(category__name=category).count()

    return render(request, 'product_by_category.html', {"page_obj":page_obj, "category": category, "num_product":num_products } )
