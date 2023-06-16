from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView


from .models import ProductCategory, Product, Basket


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context


# def index(request):
#     return render(request, 'products/index.html')


def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
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
