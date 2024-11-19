from django.contrib import admin # type: ignore
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Display 'name' and 'slug' columns in the admin list view
    prepopulated_fields = {'slug': ('name',)}  # Automatically populate the slug field based on the 'name'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available','orders','image','image2','image3','rates','created', 'updated')
    #list_filter = ('available', 'created', 'updated', 'category')  # Add filter options
    list_editable = ('price', 'stock', 'available', 'orders', 'rates')  # Make fields editable directly in the list view
    prepopulated_fields = {'slug': ('name',)}  # Automatically populate the slug field based on the 'name'
    search_fields = ('name', 'description')  # Enable search functionality for 'name' and 'description' fields



# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)