# Generated by Django 3.2.7 on 2021-09-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0007_remove_myuser_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='follow_check',
            field=models.BooleanField(default=False),
        ),
    ]