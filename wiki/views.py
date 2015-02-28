from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from wiki.models import Category, Document
import markdown


class WikiView(ListView):
    template_name = 'wiki.html'
    model = Category


class WikiCategoriesView(ListView):
    template_name = 'wiki_categories.html'
    model = Document


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
        context['markdown'] = md.convert('[TOC]\n' + self.object.content)
        return context
