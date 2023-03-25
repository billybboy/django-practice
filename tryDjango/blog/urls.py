from django.urls import path
from .views import (
    article_detail_view, 
    article_create_view,
    ArticleListView
)

app_name = 'articles'
urlpatterns = [
    path('detail', article_detail_view, name='article-detail'),
    path('create/', article_create_view),
    path('', ArticleListView.as_view(), name='article-list'),
]