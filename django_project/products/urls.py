from django.urls import path

from . import views

urlpatterns = [
    # /products
    # path("", views.product_list, name="product_list"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("products/<int:product_pk>/<slug:product_slug>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("brands/", views.BrandListView.as_view(), name="brand_list"),
    path("brands/<int:pk>/", views.BrandDetailView.as_view(), name="brand_detail"),
    # path(
    #     "<int:product_pk>/<slug:product_slug>/",
    #     views.ProductDetailView.as_view(),
    #     name="product_detail",
    # ),
]
