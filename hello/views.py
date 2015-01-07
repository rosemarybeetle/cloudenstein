import os
from django.shortcuts import render
from django.http import HttpResponse
import requests
import requests_oauthlib
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
from .models import Greeting
from .models import lastTweetId
import json
import random
from random import randint

# environmental variables - locally these are pulled from .env file. On Heroku, they need to be set using "Heroku config:set x=1111" etc.
adminURL=str(os.environ.get('adminURL',3)) # google spreadsheet feed
buttogs=str(os.environ.get('buttogs',3))
twit_api_key=str(os.environ.get('twit_api_key',3)) #cloudenstein twitter api key
twit_api_secret=str(os.environ.get('twit_api_secret',3)) #cloudenstein twitter api secret
twit_api_access_token=str(os.environ.get('twit_api_access_token',3)) #cloudenstein twitter api access token
twit_api_access_secret=str(os.environ.get('twit_api_access_secret',3)) #cloudenstein twitter api access token secret
# ----------------------

# Create your views here.
def index(request):
	#times = int(os.environ.get('TIMES',3))
	t=requests.get(adminURL)
	retrieveGoogleAdmin (adminURL)
	response = HttpResponse(sendText)
	return response

def saveTweetId(tid):
	g=1
	# temp_tweet = lastTweetId.objects.filter(id=0)
	# str(tweets[0].last_tweet_id)

def getLastTweetId():
	temp_tweet = lastTweetId.objects.filter(id=7)
	return temp_tweet

def last (tweet_id_loaded):
	global sendTextL
	sendTextL="not set"
	ra=randint(0,12000)
	try:
		lasty = lastTweetId(last_tweet_id =ra)
		lasty.save()
		sendTextL='last tweet model (test)created<br />'
	except:
		sendTextL='last tweet model (test) failed :(<br />'
	try:
		getLastTweetId()
		sendTextL='retrieved using getLastTweetId - success. tweet 7 ='+temp_tweet +'<br />'
	except:
		sendTextL='retrieved using getLastTweetId - fail.'
	global tweets
	tweets = lastTweetId.objects.all()
	global tt
	tt=tweets.count()
	sendTextL+='<br />number of stored tweets in test = '+str(tt)+"<br />"
	#sendTextL+=str(tweets)
	try:
		tweet0=lastTweetId.objects.filter(id=9)
		tweet0_val=tweet0[0].last_tweet_id
		sendTextL='single record pulled = '+tweet0_val
	except:
		sendTextL='single record pulled failed'
	try:
		sendTextL+=str(tweets[0].last_tweet_id)+'<br />'
	except:
		sendTextL+='last tweet get failed <br />'
	try:
		for e in range (0,tt-1):
			sendTextL+='tweet '+str(tweets[e].last_tweet_id)+'<br />'
	except:
		sendTextL+='failed to extract tweets using "for" loop'
	
	last_response = HttpResponse(sendTextL)
	return last_response

def home(home):
	times = int(os.environ.get('TIMES',3))
	homeText='<html><head><title>Cloudenstein</title></head><body><h1>Hello Home World</h1></body></html>'
	# home_response = HttpResponse(homeText)
	# return home_response
	search_tweets('#museum','50')
	home_response = HttpResponse(responsetext)
	return home_response

def retrieveGoogleAdmin (url):
	try:
		Ws= requests.get(url)
		yy= Ws.text
		global results
		results = yy.splitlines()
		global swCount
		swCount=len(results)
		global sendText
		sendText='' # initialise text sending variable
		tt=0
		while tt < swCount:
			sendText+=results[tt]
			sendText+='<br />'
			tt+=1
		sendText+= 'number of attributes received = '+str (swCount)+'<br /><br />Sent all from inside retrieveGoogleAdmin'
		return sendText
		# return swCount
	# end retrieveArray
	except:
		print ('Can\'t connect to admin settings - no connection') 



def db(request):

	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})

# ---------------search_tweets is from older Tweetenstein - to be modded ------------------
# ----------------------------------------------------------------------------------------
def search_tweets (term,count) : # params: term= 'what to search for' type = 'how to search' Count = 'number of tweets' (max 100)
	# 1: Get id of last tweet stored (to prevent saving multiple times)
	# 
	search_url_root='https://api.twitter.com/1.1/search/tweets.json?q=' # twitter json api query url
	x= term.find('#') # look to see what position the hashtag is 
	y=term.find('@') # look to see what position the @ sign is
	global termTXT
	term_raw=term
	if x==0 : #  this is checking if the first character is a hashtag (i.e it's a hashtag term search)
		print ('searching twitter API for hashtag: '+term)
		term2 = term.split('#')[1] # strip off the hash
		termTXT= term2 # allows the search term to be passed as a parameter
		term='%23'+term2 # add unicode for # sign (%23) if a hashtag search term
	else:
		if y==0: # next - check if @ is the first character (i.e. it is a username term)
			print ('searching twitter API for username: @'+term)
			term3 = term.split('@')[1] # strip off the @
			termTXT= term3 # allows the search term to be passed as a parameter
			term='%40'+term3 # add unicode for @ sign (%40) if a username search
		else:
			print ('searching for term: '+term) # or just search!
			termTXT= term # allows the search term to be passed as a parameter
	search_url=str(search_url_root+term+'&count='+count) # create the full search url from search term and admin setting for number of results
	print ('---------------------------')
	print ()
	try:
		auth = OAuth1(twit_api_key, twit_api_secret,twit_api_access_token,twit_api_access_secret)
		global auth_response
		global responsetext
		responsetext='' # initialise as string
		auth_response=requests.get(search_url, auth=auth)
		#responsetext=(auth_response.text)
		j = (auth_response.text)
		js = json.loads(j)
		js_dict=js
		global js_count
		js_count=len(js_dict['statuses'])# how many tweets in thi response? - double checking that number of tweets received was same as asked for (could be less occassionally)
		# responsetext=js['statuses'][0]['id']
		# return (responsetext)
		c = js_count
		x=0
		while (x<c):
			try:
				tweet_id = js['statuses'][x]['id']
				if (x==0):
					try:
						lastyT = lastTweetId(id=8,last_tweet_id =int(tweet_id))
						lastyT.save()
						sendTextL='last tweet id saved in filed lastTweetId[0]<br />'
					except:
						sendTextL='last tweet id save failed :(<br />'# saveTweetId (int(tweet_id)) #this where we need to save last known highest tweet_id
					# try:
					# 	tweetcatcher=lastTweetId(last_tweet_id=tweet_id)
					# 	tweetcatcher.save()
					# 	responsetext+="saved tweet id - <br /><br />"
					# except:
					# 	responsetext="Something broke while trying to save last_tweet_id"
					# 	return (responsetext)
					responsetext+='<h1>Results for search on term: '+term_raw+'</h1><p>'+str(c)+' tweets returned. Most recent tweet received has status id: '+str(tweet_id)+'</p>'
				name = js['statuses'][x]['user']['name']
				user = js['statuses'][x]['user']['screen_name']
				username= '@'+user
				responsetext +='<p>Tweet: #'+str(x+1)+', status_id: '+ str(tweet_id)+'<br />'
				responsetext +='From:'+username+'('+name+')<br />'
				responsetext += 'Text: "'+js['statuses'][x]['text']+'"</p>'
				
				# following line gets rid of Twitter line breaks...
				# tweet=tweet.replace("\n","")
				# tweet=tweet.replace("\"","'")
				# tweet=tweet.replace("\\","")
				
				# print (tweet)
				# fullTweet='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } '
				# fullTweet2='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } ,'
				# print ('WTF = x = '+str(x))
				# saveTweet(fullTweet)
				# saveTweet2(fullTweet2)
				# tid=int(tweet_id)
				# fullTweetCSV=str(tweet_id)+','+str(username)+','+str(name)+','+str(tweet)
				# saveTweetCSV(fullTweetCSV)
			except UnicodeEncodeError:
				responsetext="Something broike while polling through tweets. This msg inside search_tweets > inside while loop"
				return (responsetext) 
			x=x+1
		return (responsetext)
		# fullTweet2='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } ]}'
		# saveTweet2(fullTweet2)
	except KeyError:
		responsetext="Failed called to Twitter. This msg inside search_tweets"
		return (responsetext) 
	
# ------------- end search twitter -------------------------
# ---------------search_tweets is from older Tweetenstein - to be modded ------------------
# ----------------------------------------------------------------------------------------

# def retrieveLastTweet():
# 	global last_tweet_known
# 	last_tweet_known

