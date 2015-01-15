from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class lastTweetId(models.Model):
	last_tweet_id = models.BigIntegerField(max_length=20)

class lt(models.Model):
	lt1_7=models.IntegerField()
	lt_8_14=models.IntegerField()
	lt_rem=models.IntegerField()

class lt_st(models.Model):
	position=models.IntegerField()
	lt_id=models.CharField(max_length=200)

class tweet(models.Model):
	tid=models.CharField(max_length=20)
	name=models.CharField(max_length=140)
	username=models.CharField(max_length=12)
	status=models.CharField(max_length=140)
	avatar=models.CharField(max_length=140)
	hashtag_ct=models.CharField(max_length=20)
	hashtag_list=models.CharField(max_length=140)
	mention_ct=models.CharField(max_length=20)
	mention_list=models.CharField(max_length=140)
	url_ct=models.CharField(max_length=20)
	url_list=models.CharField(max_length=140)

class cloud_admin(models.Model):
	search_term=models.CharField(max_length=20) # what the api is searching for
	tweet_num=models.CharField(max_length=3) # max value = 100
	harvest_period=models.CharField(max_length=60) # in seconds
	intro_text=models.CharField(max_length=300)
	sub_text=models.CharField(max_length=300)