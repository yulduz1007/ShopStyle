from django.shortcuts import render, redirect

from apps.models import Product


# Create your views here.
def product_form_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'apps/ShopStyle.html', context=context)


def product_detail_view(request, pk):
    context = {
        'product': Product.objects.get(pk=pk)
    }
    return render(request, 'apps/ShopStyleDetail.html', context=context)




