from django.db import models

# Create your models here.
class Greeting(models.Model):
	when = models.DateTimeField('date created', auto_now_add=True)

class authed(models.Model):
	un=models.CharField(max_length=20)
	pw=models.CharField(max_length=20)


class lastTweetId(models.Model):
	last_tweet_id = models.BigIntegerField(max_length=20)

class lt(models.Model):
	lt1_7=models.IntegerField()
	lt_8_14=models.IntegerField()
	lt_rem=models.IntegerField()

class lt_st(models.Model):
	position=models.IntegerField()
	lt_id=models.CharField(max_length=200)

class last_men(models.Model):
	men_id=models.CharField(max_length=140)
	men_un=models.CharField(max_length=140)

class tweeten(models.Model):
	tid=models.CharField(max_length=140)
	t_name=models.CharField(max_length=140)
	t_username=models.CharField(max_length=140)
	t_status=models.CharField(max_length=240)
	t_avatar=models.CharField(max_length=140)

class hashtags(models.Model):
	ht_term=models.CharField(max_length=140) # actual hashtag
	ht_st=models.CharField(max_length=140) # search term used to revtrieve this hashtag originally

	# mention_ct=models.CharField(max_length=20)
	# mention_list=models.CharField(max_length=140)
	# url_ct=models.CharField(max_length=20)
	# url_list=models.CharField(max_length=140)

class cloud_admin(models.Model):
	search_term=models.CharField(max_length=20) # what the api is searching for
	tweet_num=models.CharField(max_length=3) # max value = 100
	harvest_period=models.CharField(max_length=60) # in seconds
	intro_text=models.CharField(max_length=300)
	sub_text=models.CharField(max_length=300)

class process_settings(models.Model): # settings for records in sub-content tables
	st_date=models.DateTimeField()
	end_date=models.DateTimeField()
	max_tweets=models.CharField(max_length=3)
	max_tags=models.CharField(max_length=4)
	max_mens=models.CharField(max_length=4)
	max_words=models.CharField(max_length=4)
	cnt_type=models.CharField(max_length=20)
	st=models.CharField(max_length=140)

class stop_words(models.Model): #words not to bother saving
	sw=models.CharField(max_length=20)