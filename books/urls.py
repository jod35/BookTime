from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books_home'),
    path('about/',views.about,name='books_about'),
    path('contact-us/',views.ContactUsView.as_view(),name='books_contact'),
    path('products/',views.product_list,name="products")
]