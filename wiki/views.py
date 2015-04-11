from django import forms
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
import markdown

from wiki.models import Category, Document


class WikiView(ListView):
    template_name = 'wiki.html'
    model = Category


class WikiCategoriesView(ListView):
    template_name = 'wiki_categories.html'
    model = Document

    def get_queryset(self):
        self.cat = get_object_or_404(Category, slug=self.args[0])
        return Document.objects.filter(category=self.cat).order_by('date')


class WikiArticleView(DetailView):
    model = Document
    template_name = 'wiki_article.html'

    def get_context_data(self, **kwargs):
        context = super(WikiArticleView, self).get_context_data(**kwargs)
        md = markdown.Markdown(extensions=[
            'fenced_code',
            'codehilite',
            'toc',
            'smarty',
            'meta',
            'tables',
            'footnotes',
            'abbr',
            'wikilinks'
        ])
        context['markdown'] = md.convert('[TOC] \n' + self.object.content)
        return context


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ssh, screen, linux, ...'}))


def WikiSearchView(request):
    context = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        context['form'] = form
        if form.is_valid():
            s = form.cleaned_data['search']
            context['document_list'] = Document.objects.filter(Q(title__icontains=s) | Q(content__icontains=s))
            context['search_value'] = s
    else:
        context['form'] = SearchForm()

    return render(request, 'wiki_search.html', context)

