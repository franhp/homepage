from django.shortcuts import render
from django.views.generic.base import TemplateView

class ContactView(TemplateView):
    template_name = 'contact.html'
    
    def get_context_data(self, **kwargs):
        return TemplateView.get_context_data(self, **kwargs)
    
    
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        return TemplateView.get_context_data(self, **kwargs)