from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category, name='category'),
    path('product-by-categorie/<slug:category>/', views.products_by_category, name='product_by_category')
]
