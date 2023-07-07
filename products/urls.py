from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductsListView, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', cache_page(30)(ProductsListView.as_view()), name='index'),
    path('category/<int:category_id>', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
    path('basket_delete/<int:product_id>', basket_delete, name='basket_delete'),
]
