from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    following = models.ManyToManyField(
        "self",
        related_name='followers',
        symmetrical=False,
        blank=True
        )
    posts = models.IntegerField(default=0)

    def __str__(self):
        return self.username
