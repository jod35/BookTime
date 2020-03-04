from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books_home'),
    path('about/',views.about,name='books_about'),
]