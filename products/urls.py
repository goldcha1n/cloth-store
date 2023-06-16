from django.urls import path

from .views import *

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
    path('basket_delete/<int:product_id>', basket_delete, name='basket_delete'),
]