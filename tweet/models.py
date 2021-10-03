from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from twitteruser.models import MyUser


class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    tweeted_at = models.DateTimeField(default=timezone.now)
    tweeter = models.ForeignKey(
        MyUser,
        related_name='tweeter',
        on_delete=CASCADE
        )
    tags = models.ManyToManyField(
        MyUser,
        symmetrical=False,
        related_name='tags',
        blank=True
    )

    def __str__(self):
        return self.tweet
