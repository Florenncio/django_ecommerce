from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "demo"

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.category, name="category"),
    path("product-by-categorie/<slug:category>/", views.products_by_category, name="product_by_category"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
]
