from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import ProductCategory, Product, Basket


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context


class ProductsListView(ListView):
    # Пагинация ListView происходит под капотом, нужно лишь вписать правильные названия (см. в документации)
    paginate_by = 3
    model = Product
    template_name = 'products/products.html'

    # Вывод товара по категориям, если передается category_id, иначе вывод всех товаров без фильтра
    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    # Внесение своего контекста в класс
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['title'] = 'Store - Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context


@login_required()
def basket_add(request, product_id):  # Нет смысла использовать CreateView для такой тригерной ф-ции, поэтому лучше оставить в DBV
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
