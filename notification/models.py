from django.db import models
from tweet.models import Tweet

class Notification(models.Model):
    tags = models.ManyToManyField(
        Tweet,
        symmetrical=False,
        blank=True,
        # null=True
    )
