from django.contrib import admin

from goods.models import Catagories, Products

#admin.site.register(Catagories)
#admin.site.register(Products)

@admin.register(Catagories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]
       
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}    
    list_display = ['name', 'quantity' ,'price', 'discount']
    list_editable = ['discount',]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category']
    fields = [
              'name', 
              'category',
              'slug',
              'description', 
              'image', 
              ('price', 'discount'),
              'quantity',
              ]