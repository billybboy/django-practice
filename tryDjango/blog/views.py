from django.shortcuts import render
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article

# Create your views here.
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()



def article_create_view(request):
    initial_data = {
        'title': 'My this awesome title'
    }
    context = {
        'form': form
    }
    return render(request, "blog/article_create.html", context) 


def article_detail_view(request):
    obj = Article.objects.get(id=1)
    context = {
        'title': obj.title,
        'content': obj.content
    }
    return render(request, "blog/article_details.html", context)