from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    message = forms.CharField()
