# Generated by Django 3.2.7 on 2021-09-09 23:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0009_remove_myuser_follow_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='follow_check',
            field=models.ManyToManyField(default=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
