from cgitb import reset
from pydoc import pager
from django.core.paginator import Paginator
from urllib import request
from django.shortcuts import render
from ecommerce.inventory import models

def home(request):
    return render(request, 'base.html')

def category(request):
    data = models.Category.objects.all()
    p = Paginator(data, 10)
    
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    
    return render(request, 'categories.html', {"page_obj":page_obj})

def products_by_category(request, category):

    data = models.Product.objects.filter(category__name=category)
    p = Paginator(data, 15)

    pager_number = request.GET.get('page')
    page_obj = p.get_page(pager_number)

    return render(request, 'product_by_category.html', {"page_obj":page_obj})
