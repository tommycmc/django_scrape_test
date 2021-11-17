from django.db import models
import uuid

from django.db.models.query_utils import Q

class ArticleSite:
    WEEKENDHK = 'WE'
    OPENRICE = 'OR'
    YAHOO = 'YH'
    SITES_OPTIONS = [
        (WEEKENDHK, 'Weekendhk'),
        (OPENRICE, 'OpenRice'),
        (YAHOO, 'Yahoo'),
    ]
    SITE_OPTIONS_DICT = dict(SITES_OPTIONS)

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=100, unique=True, null=False, blank=False)
    title = models.TextField(null=False, blank=False)
    created_time = models.DateTimeField()
    site = models.CharField(max_length=2, choices=ArticleSite.SITES_OPTIONS)

    content = models.TextField()

    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({ArticleSite.SITE_OPTIONS_DICT[self.site]})'

    class Meta:
        #partial index for articles in each domain
        indexes = [
            models.Index(name=f'site_index_{article_site}', fields=['site'], condition=Q(site=article_site)) for article_site in ArticleSite.SITE_OPTIONS_DICT.keys()
        ]

