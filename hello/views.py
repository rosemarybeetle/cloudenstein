import os
from django.shortcuts import render
from django.http import HttpResponse
import requests
import requests_oauthlib
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
from .models import Greeting
from .models import lastTweetId
from .models import LT
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
def tweetPackager(tid):
	global tl
	global t1_7
	global t8_14
	global trem
	strtid=str(tid)
	tl=len(strtid)
	t1_7=strtid[:7]
	t8_14=strtid[7:14]
	trem=strtid[14:tl]
	return (int(tl),int(t1_7),int(t8_14),int(trem))


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
	lasty = LT.objects.all()
	global ttt
	ttt=lasty[0].lt_id
	return ttt	

def last (tweet_id_loaded):
	global sendTextL
	ra=randint(0,12000)
	sendTextL="default trace text <br />"
	try:
		lasty = lastTweetId(last_tweet_id =ra)
		lasty.save()
		sendTextL+='last tweet model (test)created<br />'
	except Exception as e:
		sendTextL+='last tweet model (test) failed :(<br />'
	try:
		getLastTweetId()
		sendTextL+='retrieved using getLastTweetId - success. tweet 7 ='+str(ttt) +'<br />'
	except Exception as e:
		sendTextL+='retrieved using getLastTweetId - fail.'+str(e)+'<br />'
	global tweets
	tweets = lastTweetId.objects.all()
	global tt
	tt=tweets.count()
	#
	sendTextL+='<br />number of stored tweets in test = '+str(tt-1)+"<br />"
	#sendTextL+=str(tweets)
	global tweetyr
	try:
		tweetyr=lastTweetId.objects.all()
		tweet0_val=tweetyr[tt-1].last_tweet_id
		sendTextL+='single record pulled = '+str(tweet0_val)+'<br />'
	except Exception as e:
		sendTextL+='single record pulled failed<br/>'+str(e)+'<br />'
	try:
		sendTextL+='Most recent value (#'+str(tt-1)+') = '+str(tweets[tt-1].last_tweet_id)+'<br />'
	except Exception as e:
		sendTextL+='last tweet get failed <br />'+str(e)+'<br />'
	try:
		for e in range (0,tt-1):
			sendTextL+='tweet '+str(e)+' = '+str(tweets[e].last_tweet_id)+'<br />'
	except Exception as e:
		sendTextL+='failed to extract tweets using "for" loop'+str(e)+'<br />'
	
	last_response = HttpResponse(sendTextL)
	return last_response

def home(home):
	times = int(os.environ.get('TIMES',3))
	homeText='<html><head><title>Cloudenstein</title></head><body><h1>Hello Home World</h1></body></html>'
	
	search_tweets('#museum','50')

	# try:
	# 	lass = LT(lt_id=laztwt,position=0)
	# 	lass.save()
	# 	responsetext+='<br />tweet just saved = '+str(laztwt)
	# except Exception as e:
	# 	responsetext+='lass save failed'+str(laztwt)
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
	except Exception as e:
		print ('Can\'t connect to admin settings - no connection') +str(e)+'<br />'



def db(request):

	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})

# ---------------search_tweets is from older Tweetenstein - to be modded ------------------
# ----------------------------------------------------------------------------------------
def search_tweets (term,count) : # params: term= 'what to search for' type = 'how to search' Count = 'number of tweets' (max 100)
	global responsetext
	responsetext="default"
	# 1: Get id of last tweet stored (to prevent saving multiple times)
	# 
	# try:
	# 	lass = LT(lt_id=int(tweet_id),position=0)
	# 	lass.save()
	# 	responsetext+='<br />tweet just saved = '+str(tweet_id)
	# except Exception as e:
	# 	responsetext+='lastyT save failed'+str(tweet_id)
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
						tweetPackager(tweet_id)
						responsetext+='t1_7='+str(t1_7)+'<br />'
						responsetext+='t8_14='+str(t8_14)+'<br />'
						responsetext+='trem='+str(trem)+'<br /><br />'
					except Exception as e:
						responsetext+='Failed at rebuilding tweetPackager string because of error: '+str(e)+'<br /><br />'
					global laztwt
					laztwt=long(tweet_id)
					try:
						ra=randint(0,12000)
						lasty = LT(lt_1_7=t1_7,lt_8_14=t8_14,lt_rem=trem,position=0)
						lasty.save()
						responsetext+='last tweet model (test) xxxxx  created<br />'+tweet_id+'<br />'
					except Exception as e:
						responsetext+='last tweet model (test) xxxxx  failed :(<br />'+str(e)+' and '+str(laztwt)+'<br />'
					responsetext+='<h1>Results for search on term: '+term_raw+'</h1><p>'+str(c)+' tweets returned. Most recent tweet received has status id: '+str(tweet_id)+'</p>'
				name = js['statuses'][x]['user']['name']
				user = js['statuses'][x]['user']['screen_name']
				username= '@'+user
				responsetext +='<p>Tweet: #'+str(x+1)+', status_id: '+ str(tweet_id)+'<br />'
				responsetext +='From:'+username+'('+name+')<br />'
				responsetext += 'Text: "'+js['statuses'][x]['text']+'"</p><hr />'
				
				
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
			except Exception as e:
				responsetext="Something broike while polling through tweets. This msg inside search_tweets > inside while loop"+str(e)+'<br />'
				return (responsetext,laztwt) 
			x=x+1
		try:
			checkLT=LT.objects.all()
			lt=checkLT[0].lt_id
			responsetext+='Retrieved last tweet id = '+str(lt)+'<br />'
		except Exception as e:
			responsetext+='Retrieved last tweet id FAILED<br />'+str(e)+'<br />'
		return (responsetext, laztwt)
		# fullTweet2='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } ]}'
		# saveTweet2(fullTweet2)
		try:
			checkLT=LT.objects.all()
			lt=checkLT[0].lt_id
			responsetext+='Retrieved last tweet id = '+str(lt)+'<br />'
		except Exception as e:
			responsetext+='Retrieved last tweet id FAILED<br />'
	except Exception as e:
		responsetext="Failed called to Twitter. This msg inside search_tweets"+str(e)+'<br />'
		return (responsetext) 
	
# ------------- end search twitter -------------------------
# ---------------search_tweets is from older Tweetenstein - to be modded ------------------
# ----------------------------------------------------------------------------------------

# def retrieveLastTweet():
# 	global last_tweet_known
# 	last_tweet_known

