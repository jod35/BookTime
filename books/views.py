from django.shortcuts import render
from django.views.generic import FormView,ListView
from django.shortcuts import get_object_or_404
from . import models
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

class ProductListView(ListView):
    template_name='books/product_list.html'
    paginate_by=4


    def query_set(self):
        tag=self.kwargs['tag']
        self.tag=None

        if tag !='all':
            self.tag=get_object_or_404(models.ProductTag,slug=tag)

        if self.tag:
            products=models.Product.objects.active().filter(tags=self.tags)
        else:
            products=models.Products.objects.active()

        return products.order_by('name')
