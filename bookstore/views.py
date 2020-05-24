from django.shortcuts import render
from .models import Book
from django.views.generic import ListView


class BookListView(ListView):
    template_name='bookstore/index.html'
    model=Book
    paginate_by=6
    # context_object_name='books'



def book_details(request,title):
    book=Book.objects.get(title=title)
    context={
        'book':book
    }

    return render(request,'bookstore/book_detail.html',context)


def loginView(request):
    return render(request,'bookstore/login.html')


def signUpView(request):
    return render(request,'bookstore/register.html')