from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product


def product_list(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    return render(
        request,
        "products/product_list.html",
        context={"products": products},
    )

def product_derail(request: HttpRequest, product_pk: int, product_slug: str) -> HttpRequest:
    product = Product.objects.filter(pk=product_pk, slug=product_slug).get()
    return render(
        request,
        template_name="products/product_derail.html",
        context={"product": product}
    )

def about(request: HttpRequest, ) -> HttpRequest:
    product = Product.objects.filter().all()
    return render(
        request,
        template_name="products/about.html"
    )