import os
from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
from .models import Greeting

adminURL=str(os.environ.get('adminURL',3)) # now pulled in more securely (or at least could be...)
buttogs=str(os.environ.get('buttogs',3))
twit_api_key=str(os.environ.get('twit_api_key',3)) #cloudenstein twitter api key
twit_api_secret=str(os.environ.get('twit_api_secret',3)) #cloudenstein twitter api secret
twit_api_access_token=str(os.environ.get('twit_api_access_token',3)) #cloudenstein twitter api access token
twit_api_access_secret=str(os.environ.get('twit_api_access_secret',3)) #cloudenstein twitter api access token secret

# Create your views here.
def index(request):
	#times = int(os.environ.get('TIMES',3))
	t=requests.get(adminURL)
	retrieveGoogleAdmin (adminURL)
	response = HttpResponse(sendText)
	return response

	
def home(home):
	times = int(os.environ.get('TIMES',3))
	homeText='<html><head><title>Cloudenstein</title></head><body><h1>Hello Home World</h1></body></html>'
	# home_response = HttpResponse(homeText)
	# return home_response
	search_tweets('#museum','50')
	home_response = HttpResponse(auth_response.text)
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
		auth_response=requests.get(search_url, auth=auth)
		responsetext=(auth_response.text)
		return (responsetext)
		j = (auth_response.text)
		# js = json.loads(j)
		# c = int(count)
		# x=0
		# while (x<c-1):
		#     try:
		#         tweet_id = js['statuses'][x]['id']
		#         testID=int(tweet_id)
		#         print ('testID= '+str(testID))
		#         print('-------')
		#         print ('---------------')
		#         if (x==0):
		#             saveTweetId (str(tweet_id))
		#         print ('Tweet '+str(x+1)+' of '+str(c)+'. Tweet id: '+str(tweet_id))
		#         name = js['statuses'][x]['user']['name']
		#         user = js['statuses'][x]['user']['screen_name']
		#         username= '@'+user
		#         print ('From:'+username+'('+name+')')
		#         tweet = js['statuses'][x]['text']
		#         # following line gets rid of Twitter line breaks...
		#         tweet=tweet.replace("\n","")
		#         tweet=tweet.replace("\"","'")
		#         tweet=tweet.replace("\\","")
				
		#         print (tweet)
		#         fullTweet='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } '
		#         fullTweet2='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } ,'
		#         print ('WTF = x = '+str(x))
		#         saveTweet(fullTweet)
		#         saveTweet2(fullTweet2)
		#         tid=int(tweet_id)
		#         fullTweetCSV=str(tweet_id)+','+str(username)+','+str(name)+','+str(tweet)
		#         saveTweetCSV(fullTweetCSV)                
		#     except UnicodeEncodeError:
		#         print ('Tweet text not available - dodgy term in tweet broke the API')
		#         print ('---------------')
		#     x=x+1
		# fullTweet2='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } ]}'
		# saveTweet2(fullTweet2)
	except KeyError:
		responsetext="Failed called to Twitter. This msg inside search_tweets"
		return (responsetext) # - uncomment to check the text is returning as expected
	
# ------------- end search twitter -------------------------
# ---------------search_tweets is from older Tweetenstein - to be modded ------------------
# ----------------------------------------------------------------------------------------



