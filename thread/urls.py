from django.urls import path
from .views import getForumUsers, getEmojis, getThreads, getThread, getComment, getComments

urlpatterns = [
    path('forum/users', getForumUsers),
    path('forum/emojis', getEmojis),
    path('forum/threads', getThreads),
    path('forum/thread/<str:id>', getThread),
    path('forum/comment/comments', getComments),
    path('forum/comment/<str:id>', getComment),
]
