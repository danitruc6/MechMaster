# Generated by Django 4.2.2 on 2023-07-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0017_forumcategory_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumcategory',
            name='category_image',
            field=models.URLField(default='https://thumbs.dreamstime.com/b/no-image-available-icon-flat-vector-no-image-available-icon-flat-vector-illustration-132482953.jpg'),
        ),
    ]
