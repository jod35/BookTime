from django.urls import path
from . import views


app_name='bookstore'

urlpatterns = [
    path('',views.BookListView.as_view(),name='home'),
    path('details/<str:title>/',views.book_details,name='details'),
]