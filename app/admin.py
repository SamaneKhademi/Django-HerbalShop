from django.contrib import admin
from .models import Product, Customer, Cart, Wishlist, BlogPost

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'selling_price', 'discounted_price', 'category', 'product_image')

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'mobile', 'state', 'city', 'locality', 'zipcode')

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')

@admin.register(BlogPost)
class BlogPostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image')
