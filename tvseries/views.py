from django.shortcuts import render
from django.views.generic.base import TemplateView


class TVSeriesView(TemplateView):
    '''
    Test
    '''
    
    template_name = 'tvseries.html'
    
    def get_context_data(self, **kwargs):
        return TemplateView.get_context_data(self, **kwargs)
