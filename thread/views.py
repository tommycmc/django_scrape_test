from django.shortcuts import render

from .serializers import ForumUserSerializer, EmojiSerializer, CommentSerializer, ThreadSerializer

# Create your views here.
from .models import ForumUser, Emoji, Comment, Thread
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getForumUsers(req):
    forumUsers = ForumUser.objects.all()
    forumUserSerializer = ForumUserSerializer(forumUsers, many=True)
    return Response(forumUserSerializer.data)

@api_view(['GET'])
def getEmojis(req):
    emojis = Emoji.objects.all()
    emojiSerializer = EmojiSerializer(emojis, many=True)
    return Response(emojiSerializer.data)

@api_view(['GET'])
def getComments(req):
    comments = Comment.objects.all()
    commentSerializer = CommentSerializer(comments, many=True)
    return Response(commentSerializer.data)

@api_view(['GET'])
def getComment(req, id):
    comment = Comment.objects.get(id=id)
    commentSerializer = CommentSerializer(comment, many=False)
    return Response(commentSerializer.data)

@api_view(['GET'])
def getThreads(req):
    threads = Thread.objects.all()
    threadSerializer = ThreadSerializer(threads, many=True)
    return Response(threadSerializer.data)

@api_view(['GET'])
def getThread(req, id):
    thread = Thread.objects.get(id=id)
    threadSerializer = ThreadSerializer(thread, many=False)
    return Response(threadSerializer.data)
