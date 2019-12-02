from django.db import models
from django.utils import timezone
from twitterclone.twitterusers.models import TwitterUser


class Tweet(models.Model):
    twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    posts = models.CharField(max_length=140)
    time_date = models.DateTimeField(default=timezone.now)