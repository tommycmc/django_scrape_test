from django.contrib import admin
from thread.models import ForumUser, Emoji, Comment, Thread
from django.utils.safestring import mark_safe

# class CommentAdmin(admin.ModelAdmin):
#     # model = Comment
#     # filter_horzontal = ('emoji')
    
#     list_display = ('created_user', 'content', 'post_position', 'created_time', 'thread')

#     pass

class EmojiAdmin(admin.ModelAdmin):
    def emoji_image(self, obj):   
        return mark_safe(f'<img src="{obj.icon_url}"/>')

    list_display = ('emoji_image', 'tag_name', 'site')

class CommentAdmin(admin.StackedInline):
    model = Comment

    # list_display = ('thread', 'post_position', 'created_user', 'created_time')


    # created_user = models.ForeignKey(ForumUser, on_delete=models.CASCADE)
    # content = models.TextField(null=False, blank=True)
    # post_position = models.PositiveIntegerField()
    # emoji = models.ManyToManyField(Emoji, null=True, blank=True)
    # created_time = models.DateTimeField()

    # thread



# Register your models here.
admin.site.register(ForumUser)
admin.site.register(Emoji, EmojiAdmin)
admin.site.register(Comment)
admin.site.register(Thread)