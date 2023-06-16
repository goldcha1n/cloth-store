from django.urls import path

from .views import *

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>', products, name='category'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
    path('basket_delete/<int:product_id>', basket_delete, name='basket_delete'),
]