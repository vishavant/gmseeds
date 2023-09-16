from django.contrib import admin
from .models import ProductCategory, Product, ContactUs
# Register your models here.


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product_cat_id', 'product_category_name', 'product_category_image', 'product_description', 'is_active', 'created_at', 'updated_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_category', 'product_name', 'product_short_description', 'product_image', 'product_discount_price', 'product_price']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['contact_id', 'contact_name', 'mobile', 'email', 'query_type', 'message', 'created_at', 'updated_at']


    


