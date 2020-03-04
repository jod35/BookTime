from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from books import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='books/index.html'))
]
