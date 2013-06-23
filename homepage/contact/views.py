from django.shortcuts import render_to_response
from django.template.context import RequestContext
from contact.models import ContactForm
from django.core.mail import mail_admins


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            mail_admins('Message from ' + name, message + '\nYou can contact me at: ' + email)
            return render_to_response('thanks.html', RequestContext(request, {'name': name}))
    return render_to_response('contact.html', RequestContext(request, {}))
