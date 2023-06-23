from django.contrib import admin

from .models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # Отображается на админ странице продукто
    fields = ('name',
              'description',
              ('price', 'quantity'),
              'image',
              'category')  # Отображается на админ странице продуктов #, Чтобы отображать на одной странице два поля,
    # нужно использовать кортеж внутри кортежа
    # readonly_fields = ('description',) Вывод поля только для чтения, В кортеже с одним полем нужно использовать
    # запятую, иначе будет ошибка.
    search_fields = ('name',)  # Используется для поиска записей по полю.
    ordering = ('name',)  # Сортировка по названию


class BasketAdmin(admin.TabularInline):  # TabularInline Админка, которая является частью другой админки
    model = Basket
    fields = ('product', 'quantity')
