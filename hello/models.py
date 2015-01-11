from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class lastTweetId(models.Model):
	last_tweet_id = models.BigIntegerField(max_length=20)

class LT(models.Model):
	lt_1_7=models.IntegerField()
	lt_8_15=models.IntegerField()
	lt_rem=models.IntegerField()
	position=models.IntegerField()