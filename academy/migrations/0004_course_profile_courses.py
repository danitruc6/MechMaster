# Generated by Django 4.2.1 on 2023-06-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='courses',
            field=models.ManyToManyField(related_name='profiles', to='academy.course'),
        ),
    ]
