from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class lastTweetId(models.Model):
	last_tweet_id = models.IntegerField()
