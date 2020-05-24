from django.urls import path
from . import views


app_name='bookstore'

urlpatterns = [
    path('',views.BookListView.as_view(),name='home'),
    path('<str:title>/details',views.book_details,name='details'),
]