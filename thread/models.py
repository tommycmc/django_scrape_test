from django.db import models
from django.db.models.query_utils import Q
import uuid

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
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)

    def __str__(self):
        return self.username

class Emoji(models.Model):
    #default field: id = models.BigAutoField(primary_key=True)
    icon = models.CharField(max_length=10, unique=True, null=False, blank=False)
    cldr_name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.icon} ({self.cldr_name})'

class Thread(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=100, unique=True)
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    like_count = models.PositiveIntegerField(null=True, blank=True)
    dislike_count = models.PositiveIntegerField(null=True, blank=True)
    comment_count = models.PositiveIntegerField(null=True, blank=True)
    view_count = models.PositiveIntegerField(null=True, blank=True)

    created_time = models.DateTimeField()
    reply_time = models.DateTimeField()

    created_user = models.OneToOneField(ForumUser, on_delete=models.CASCADE)

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
    created_user = models.OneToOneField(ForumUser, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=True)
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE, null=True, blank=True)
    created_time = models.DateTimeField()

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.thread} #{self.id}'
