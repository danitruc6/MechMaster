# Generated by Django 4.2.2 on 2023-08-20 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0023_profile_profile_pic_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
    ]
