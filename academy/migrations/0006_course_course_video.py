# Generated by Django 4.2.2 on 2023-06-28 00:30

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0005_course_course_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_video',
            field=embed_video.fields.EmbedVideoField(default=False),
            preserve_default=False,
        ),
    ]
