from django.db import models
from django.db.models.query_utils import Q
import uuid
from django.utils.safestring import mark_safe

class ThreadSite:
    BABYDISCUSS = 'BD'
    BABYKINGDOM = 'BK'
    DISCUSS = 'DS'
    HKGALDEN = 'HA'
    HKGOLDEN = 'HO'
    LIHKG = 'LI'
    UWANTS = 'UW'

    SITES_OPTIONS = [
        (BABYDISCUSS, 'BabyDiscuss'),
        (BABYKINGDOM, 'BabyKingdom'),
        (DISCUSS, 'Discuss'),
        (HKGALDEN, 'Hkgalden'),
        (HKGOLDEN, 'Hkgolden'),
        (LIHKG, 'LiHKG'),
        (UWANTS, 'Uwants'),
    ]
    SITE_OPTIONS_DICT = dict(SITES_OPTIONS)

class ForumUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    forum_id = models.CharField(max_length=50, null=False, blank=False)
    site = models.CharField(max_length=2, choices=ThreadSite.SITES_OPTIONS)
    username = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        unique_together = (('forum_id', 'site'),)

    def __str__(self):
        return self.username

class Emoji(models.Model):
    #default field: id = models.BigAutoField(primary_key=True)
    icon_url = models.CharField(max_length=500, unique=True, null=False, blank=False)
    tag_name = models.CharField(max_length=50, unique=False, null=False, blank=False)
    site = models.CharField(max_length=2, choices=ThreadSite.SITES_OPTIONS)

    def image_tag(self):
        return mark_safe(f'<div>{self.tag_name}, {ThreadSite.SITE_OPTIONS_DICT[self.site]}    <img src="{self.icon_url}" style="width: 25px; height:25px;" /></div>')


    def __str__(self):
        return mark_safe(f'<div>{self.tag_name}, {ThreadSite.SITE_OPTIONS_DICT[self.site]}    <img src="{self.icon_url}" style="width: 25px; height:25px;" /></div>')
        # return f'{self.icon_url} ({self.tag_name})'

class Thread(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=500, unique=True)
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=True)

    like_count = models.PositiveIntegerField(null=True, blank=True)
    dislike_count = models.PositiveIntegerField(null=True, blank=True)
    comment_count = models.PositiveIntegerField(null=True, blank=True)
    view_count = models.PositiveIntegerField(null=True, blank=True)

    created_time = models.DateTimeField()
    reply_time = models.DateTimeField()

    created_user = models.ForeignKey(ForumUser, on_delete=models.CASCADE)

    site = models.CharField(max_length=2, choices=ThreadSite.SITES_OPTIONS)

    def __str__(self):
        return f'{self.title} ({ThreadSite.SITE_OPTIONS_DICT[self.site]})'

    class Meta:
        #partial index for articles in each domain
        indexes = [
            models.Index(name=f'site_index_{article_site}', fields=['site'], condition=Q(site=article_site)) for article_site in ThreadSite.SITE_OPTIONS_DICT.keys()
        ]


class Comment(models.Model):
    #default field: id = models.BigAutoField(primary_key=True)
    created_user = models.ForeignKey(ForumUser, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=True)
    post_position = models.PositiveIntegerField()
    emoji = models.ManyToManyField(Emoji, null=True, blank=True)
    created_time = models.DateTimeField()

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.thread} #{self.post_position}'
1