from django.urls import path
from .views import getAuthors, getArticles, getArticle

urlpatterns = [
    path('article/authors', getAuthors),
    path('article/articles', getArticles),
    path('article/<str:id>', getArticle),
]
