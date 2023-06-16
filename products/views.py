from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import ProductCategory, Product, Basket


def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'products/products.html', context)


@login_required()
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():  # Если не существует в корзине выбранного товара
        Basket.objects.create(user=request.user, product=product,
                              quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required()
def basket_delete(request, product_id):
    baskets = Basket.objects.filter(id=product_id)
    baskets.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
