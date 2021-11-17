# Generated by Django 3.2.9 on 2021-11-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0002_emoji_cldr_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='comment_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='dislike_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='like_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='view_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
