from django.shortcuts import render,redirect
from .models import Book
from django.views.generic import ListView
from .forms import UserRegisterForm,BookCreationForm,ReviewForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


#List of all books
class BookListView(ListView):
    template_name='bookstore/index.html'
    model=Book
    paginate_by=6
    # context_object_name='books'


#Book Details
def book_details(request,id):
    book=Book.objects.get(id=id)
    tags=Book.tags.all()
    form=ReviewForm()

    context={
        'form':form,
        'book':book,
        'tags':tags
    }

    return render(request,'bookstore/book_detail.html',context)

#logout
def logout(request):
    return render(request,'bookstore/loggedout.html')

#Signup View
def signUpView(request):
    form=UserRegisterForm()

    if request.method=='POST':
        form=UserRegisterForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

    context={
        'form':form
    }
    return render(request,'bookstore/register.html',context)

#Create A Book
@login_required
def create_book(request):

    form = BookCreationForm()

    if request.method =='POST':
        form=BookCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Added Successfully')
            return redirect('bookstore:home')
    

    context={
        'form':form
    }
    return render(request,'bookstore/add_book.html',context)


#updatebook info
@login_required
def update_book_info(request,id):
    book=Book.objects.get(id=id)

    context={
        'book':book
    }

    return render(request,'bookstore/update_book.html',context)