from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)    

class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    template_name = 'articles/article_create.html'
    queryset = Article.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    template_name = 'articles/article_details.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
    def get_success_url(self):
        return reverse('articles:article-list')
