from django.contrib.postgres.aggregates import ArrayAgg
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from ecommerce.inventory import models


def home(request):
    return render(request, "base.html")


def category(request):
    data = models.Category.objects.annotate(Count("product")).order_by("-product__count")
    p = Paginator(data, 10)

    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)

    num_categories = models.Category.objects.count()

    return render(request, "categories.html", {"page_obj": page_obj, "num_category": num_categories})


def products_by_category(request, category):

    data = models.Product.objects.filter(category__name=category).values(
        "id",
        "name",
        "slug",
        "description",
        "category__name",
        "product__store_price",
        "product__sku",
        "product__product_inventory__units",
    )
    p = Paginator(data, 42)

    pager_number = request.GET.get("page")
    page_obj = p.get_page(pager_number)

    num_products = models.Product.objects.filter(category__name=category).count()

    return render(
        request, "product_by_category.html", {"page_obj": page_obj, "category": category, "num_product": num_products}
    )


def product_detail(request, slug):

    filter_arguments = []

    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)

        obj = (
            models.ProductInventory.objects.filter(product__slug=slug)
            .filter(attribute_values__attribute_value__in=filter_arguments)
            .annotate(num_tags=Count("attribute_values"))
            .filter(num_tags=len(filter_arguments))
            .values(
                "sku",
                "weight",
                "store_price",
                "product__slug",
                "product__description",
                "product__name",
                "brand__name",
                "product__category__name",
                "product__category__slug",
                "product_inventory__units",
            )
            .annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
            .get()
        )
    else:
        obj = (
            (
                models.ProductInventory.objects.filter(product__slug=slug)
                .filter(is_default=True)
                .values(
                    "sku",
                    "weight",
                    "store_price",
                    "product__slug",
                    "product__description",
                    "product__name",
                    "brand__name",
                    "product__category__name",
                    "product__category__slug",
                    "product_inventory__units",
                )
            )
            .annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
            .get()
        )

    inventory_attr = (
        models.ProductInventory.objects.filter(product__slug=slug)
        .distinct()
        .values(
            "attribute_values__product_attribute__name",
            "attribute_values__attribute_value",
        )
    )

    type_attr = (
        models.ProductTypeAttribute.objects.filter(product_type__product_type__product__slug=slug)
        .distinct()
        .values(
            "product_attribute__name",
        )
    )

    return render(
        request, "product_detail.html", {"obj": obj, "inventory_attr": inventory_attr, "type_attr": type_attr}
    )
