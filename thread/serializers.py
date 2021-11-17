from rest_framework.serializers import ModelSerializer
from .models import ForumUser, Emoji, Comment, Thread

class ForumUserSerializer(ModelSerializer):
    class Meta:
        model = ForumUser
        fields = '__all__'

class EmojiSerializer(ModelSerializer):
    class Meta:
        model = Emoji
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ThreadSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'
