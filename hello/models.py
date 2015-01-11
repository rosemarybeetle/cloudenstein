from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class lastTweetId(models.Model):
	last_tweet_id = models.BigIntegerField(max_length=20)

class lt(models.Model):
	lt1_7=models.IntegerField()
	lt_8_14=models.IntegerField()
	lt_rem=models.IntegerField(max_length=200)

class lt_st(models.Model):
	position=models.IntegerField()
	lt_id=models.CharField()