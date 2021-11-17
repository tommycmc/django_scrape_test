from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Author, Article

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
