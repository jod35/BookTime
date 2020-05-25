from django.shortcuts import render,redirect
from .models import Book
from django.views.generic import ListView
from .forms import UserRegisterForm,BookCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

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


def logout(request):
    return render(request,'bookstore/loggedout.html')


def signUpView(request):
    form=UserRegisterForm()

    if request.method=='POST':
        form=UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

    context={
        'form':form
    }
    return render(request,'bookstore/register.html',context)

@login_required
def create_book(request):

    form = BookCreationForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request,'Book Added Successfully')
        return redirect('bookstore:home')
        

   
    context={
        'form':form
    }
    return render(request,'bookstore/add_book.html',context)