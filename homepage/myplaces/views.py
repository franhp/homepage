from django.shortcuts import render
from django.views.generic.base import TemplateView


class MyPlacesView(TemplateView):
    '''
    Test
    '''
    
    template_name = 'myplaces.html'
    
    def get_context_data(self, **kwargs):
        return TemplateView.get_context_data(self, **kwargs)
