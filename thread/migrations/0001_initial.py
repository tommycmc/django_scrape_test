# Generated by Django 3.2.9 on 2021-12-26 10:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_url', models.CharField(max_length=100, unique=True)),
                ('tag_name', models.CharField(max_length=50, unique=True)),
                ('site', models.CharField(choices=[('BD', 'BabyDiscuss'), ('BK', 'BabyKingdom'), ('DS', 'Discuss'), ('HA', 'Hkgalden'), ('HO', 'Hkgolden'), ('LI', 'LiHKG'), ('UW', 'Uwants')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ForumUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('forum_id', models.CharField(max_length=50, unique=True)),
                ('site', models.CharField(choices=[('BD', 'BabyDiscuss'), ('BK', 'BabyKingdom'), ('DS', 'Discuss'), ('HA', 'Hkgalden'), ('HO', 'Hkgolden'), ('LI', 'LiHKG'), ('UW', 'Uwants')], max_length=2)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100, unique=True)),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('like_count', models.PositiveIntegerField(blank=True, null=True)),
                ('dislike_count', models.PositiveIntegerField(blank=True, null=True)),
                ('comment_count', models.PositiveIntegerField(blank=True, null=True)),
                ('view_count', models.PositiveIntegerField(blank=True, null=True)),
                ('created_time', models.DateTimeField()),
                ('reply_time', models.DateTimeField()),
                ('site', models.CharField(choices=[('BD', 'BabyDiscuss'), ('BK', 'BabyKingdom'), ('DS', 'Discuss'), ('HA', 'Hkgalden'), ('HO', 'Hkgolden'), ('LI', 'LiHKG'), ('UW', 'Uwants')], max_length=2)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thread.forumuser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('post_position', models.PositiveIntegerField()),
                ('created_time', models.DateTimeField()),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thread.forumuser')),
                ('emoji', models.ManyToManyField(blank=True, null=True, to='thread.Emoji')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thread.thread')),
            ],
        ),
        migrations.AddIndex(
            model_name='thread',
            index=models.Index(condition=models.Q(('site', 'BD')), fields=['site'], name='site_index_BD'),
        ),
        migrations.AddIndex(
            model_name='thread',
            index=models.Index(condition=models.Q(('site', 'BK')), fields=['site'], name='site_index_BK'),
        ),
        migrations.AddIndex(
            model_name='thread',
            index=models.Index(condition=models.Q(('site', 'DS')), fields=['site'], name='site_index_DS'),
        ),
        migrations.AddIndex(
            model_name='thread',
            index=models.Index(condition=models.Q(('site', 'HA')), fields=['site'], name='site_index_HA'),
        ),
        migrations.AddIndex(
            model_name='thread',
            index=models.Index(condition=models.Q(('site', 'HO')), fields=['site'], name='site_index_HO'),
        ),
        migrations.AddIndex(
            model_name='thread',
            index=models.Index(condition=models.Q(('site', 'LI')), fields=['site'], name='site_index_LI'),
        ),
        migrations.AddIndex(
            model_name='thread',
            index=models.Index(condition=models.Q(('site', 'UW')), fields=['site'], name='site_index_UW'),
        ),
    ]
