# Generated by Django 4.2.2 on 2023-07-15 01:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0014_forumtopic_likes_forumtopic_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumtopic',
            name='post_liked',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
