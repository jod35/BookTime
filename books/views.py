from django.shortcuts import render
from django.views.generic import FormView
from.import forms

# Create your views here.

def home(request):
    return render(request,'books/index.html')

def about(request):
    return render(request,'books/about.html')

class ContactUsView(FormView):
    template_name='books/contact_form.html'
    form_class=forms.ContactForm
    success_url='/'

    def form_valid(self,form):
        form.send_mail()
        return super().form_valid(form)