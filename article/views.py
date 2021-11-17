from django.shortcuts import render

from .serializers import AuthorSerializer, ArticleSerializer

# Create your views here.
from .models import Author, Article
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getAuthors(req):
    authors = Author.objects.all()
    authorSerializer = AuthorSerializer(authors, many=True)
    return Response(authorSerializer.data)

@api_view(['GET'])
def getArticles(req):
    articles = Article.objects.all()
    articleSerializer = ArticleSerializer(articles, many=True)
    return Response(articleSerializer.data)

@api_view(['GET'])
def getArticle(req, id):
    articles = Article.objects.get(id=id)
    articleSerializer = ArticleSerializer(articles, many=False)
    return Response(articleSerializer.data)
