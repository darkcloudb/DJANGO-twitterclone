# Generated by Django 3.2.7 on 2021-09-09 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0008_myuser_follow_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='follow_check',
        ),
    ]