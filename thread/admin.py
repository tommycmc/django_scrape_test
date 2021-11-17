from django.contrib import admin
from thread.models import ForumUser, Emoji, Comment, Thread

# Register your models here.
admin.site.register(ForumUser)
admin.site.register(Emoji)
admin.site.register(Comment)
admin.site.register(Thread)