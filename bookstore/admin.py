from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','written','created','uploaded_by','thumbnail')
    list_filter=('written','created')
    search_fields=('author','title')
    