from django.contrib import admin
from .models import Product, Customer

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'selling_price', 'discounted_price', 'category', 'product_image')

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'state', 'zipcode')