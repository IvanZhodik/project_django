from django.contrib import admin
from .models import Category, Subcategory, Subsubcategory, Brand,  Product,  Product_image

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['category']
admin.site.register(Subcategory, SubcategoryAdmin)

class SubsubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'subcategory']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['subcategory']
admin.site.register(Subsubcategory, SubsubcategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','rating','brand',  'slug', 'price', 'stock', 'available', 'subsubcategory']
    list_filter = [ 'brand', 'subsubcategory']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class Product_imageAdmin(admin.ModelAdmin):
    list_display = ['id','rating','product', 'size', 'image' ]
    list_filter = ['product']
admin.site.register(Product_image, Product_imageAdmin)