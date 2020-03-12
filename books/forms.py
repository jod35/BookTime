from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="Your Name",max_length=200)
    message=forms.CharField(label="Your Message",widget=forms.Textarea)
    