from django import forms
from django.core.mail import send_mail
import logging

logging=logging.getLogger(__name__)

class ContactForm(forms.Form):
    name=forms.CharField(label="Your Name",max_length=200)
    message=forms.CharField(label="Your Message",widget=forms.Textarea)
    

    def send_mail(self):
        logging.info("Sending Email to customer service")
        message="From {0}\n{1}".format(self.cleaned_data['name'],self.cleaned_data['message'],)
