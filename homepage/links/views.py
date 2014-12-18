from django.shortcuts import render
from django.views.generic.base import TemplateView


class LinksView(TemplateView):
    '''
    link
    '''
    
    template_name = 'links.html'
    
    def get_context_data(self, **kwargs):
        return TemplateView.get_context_data(self, **kwargs)
