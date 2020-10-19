from datetime import datetime

from apps.articles.forms import ContactForm
from apps.articles.models import Article, Comment
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import (
    DetailView, FormView, ListView, TemplateView, CreateView, UpdateView, DeleteView)
from DjangoClass.mixins import PublicMixin, PageTitleMixin
from django.urls import reverse_lazy


def index(request):
    return render(request, 'articles/list.html', {})


"""
                                  General View In Django 
import :
from apps.articles.forms import ContactForm from django.views import View
from apps.articles.forms import ContactForm
from apps.articles.models import Article
from DjangoClass.mixins import PageTitleMixin
class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'articles/list.html', {'now': datetime.now()})


"""

"""
                     TemplateView In Django 
    import : from django.views.generic import TemplateView
    class MyView(TemplateView):
        template_name = "articles/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        context['message'] = 'This is the TempleteView'
        return context

"""
"""
                    FormView In Django
    import : from django.views.generic import FormView

    class ArticleFormView(FormView):
        template_name = 'articles/create_articles.html'
        form_class = ContactForm
        # success_url = '/articles/'
        def get_success_url(self):
            return reverse('articles:list')


    
    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        return super().form_valid(form)


"""
"""
conversion Class Based View :

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }
        return render(request, 'articles/list.html', context=context)

                                 /////////////////////////////////
    
class ArticleView(TemplateView):
    template_name = "articles/list.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        articles = Article.objects.all()
        context['articles'] = articles
        return context

                                    /////////////////////////////////

class ArticleView(ListView):
    model = Article
    queryset=Article.objects.filter(is_public = True)
    context_object_name = 'articles'
    template_name='articles/list.html'

    
    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['page_title'] = 'Article List Page'
        return context
    

"""


class ArticleView(PageTitleMixin, PublicMixin, ListView):
    model = Article
    page_title = 'Article List Page'
    template_name = 'articles/list.html'


class ArticleDetailView(PageTitleMixin, DetailView):
    model = Article
    template_name = "articles/detail.html"
    query_pk_and_slug = True

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        self.page_title = obj.title
        return obj


class ArticleCreateView(PageTitleMixin, CreateView):
    model = Article
    fields = ('title', 'body', 'is_public')
    success_url = reverse_lazy('articles:list')
    template_name = "articles/create.html"
    page_title = 'Create an Article'


class ArticleUpdateView(PageTitleMixin, UpdateView):
    model = Article
    fields = ('title', 'body', 'is_public')
    success_url = reverse_lazy('articles:list')
    template_name = "articles/update.html"
    query_pk_and_slug = True

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        self.page_title = obj.title
        return obj


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:list')
    query_pk_and_slug = True
    template_name = "articles/delete.html"


class CommentCreateView(CreateView):
    model = Comment
    fields = ('article', 'comment')
    template_name = "articles/comment.html"
    success_url = reverse_lazy('articles:list')
    query_pk_and_slug = True
