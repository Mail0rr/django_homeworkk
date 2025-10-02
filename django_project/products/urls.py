from django.urls import path

from . import views

urlpatterns = [
    # /products
    path("", views.product_list, name="product_list"),
    path(
        "<int:product_pk>/<slug:product_slug>/",
        views.product_derail,
        name="product_detail"
    ),
    path("about/", views.about, name="about")
]
