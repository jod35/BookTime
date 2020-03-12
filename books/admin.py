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

class ProductImageAdmin(admin.ModelAdmin):
    list_display=('thumbnail_tag','product_name')
    readonly_fields=('thumbnails',)
    search_fields=('product__name',)


    def thumbnail_tag(self,obj):
        return format_html("<img src="%">"%obj.thumbnail.url)
        return "-"
    
    thumbnail_tag.short_description="Thumbnail"

    def product_name(self,obj):
        return obj.product.name



# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage,ProductImageAdmin)
admin.site.register(ProductTag)