# Generated by Django 3.2.7 on 2021-09-09 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0002_alter_myuser_follower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='follower',
        ),
    ]