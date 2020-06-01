from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name='bookstore'

urlpatterns = [
    path('',views.BookListView.as_view(),name='home'),
    path('details/<int:id>book/',views.book_details,name='details'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='bookstore/loggedout.html'),name='logout'),
    path('register/',views.signUpView,name='register'),
    path('add_book/',views.create_book,name="add_book"),
    path('update/<int:id>/book/',views.update_book_info,name='update_book'),
    path('books/<str:tag>/',views.search_tag,name='tag_results'),
    path('mybooks/',views.users_books,name='my_books'),
]