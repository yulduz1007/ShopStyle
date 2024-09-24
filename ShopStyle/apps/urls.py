from django.urls import path

from apps.views import product_form_view, product_detail_view

urlpatterns = [
    path('', product_form_view, name='product_form'),
    path('product-detail/<int:pk>', product_detail_view, name='product-detail'),
]
