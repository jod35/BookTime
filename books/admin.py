from django.contrib import admin
from .models import ProductTag,ProductImage,Product
from django.utils.html import format_html

#some customizations
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','slug','in_stock','price')
    list_filter=('active','in_stock','date_updated')
    list_editable=('in_stock')
    search_fields=('name',)
    prepopulated_fields={'slug':"name"}



# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductTag)