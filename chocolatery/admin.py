from django.contrib import admin

from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'content','price', 'price_with_sale', 'is_available', 'weight')
    list_display_links = ('id', 'title')
    search_fields = ('titile', 'content')
    list_editable = ('is_available',)
    list_filter = ('is_available', 'category')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('titile',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
