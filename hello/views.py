import os
from django.shortcuts import render
from django.http import HttpResponse
import requests
import requests_oauthlib
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
from .models import Greeting
from .models import lastTweetId
from .models import lt
from .models import lt_st
from .models import cloud_admin
from .models import tweet
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
debug='yes' # use this to turn on and off daft error messages
tweets='global default'
# ----------------------
# Twitter search admin settings
global t_st # tweet search term
global t_sn # tweet search number (how many tweets to return)
global t_hp # tweet harvet period. How frequently to check
global t_it # tweet intro text
global t_ot # tweet outro text
t_st='#pugs' # random default value
t_sn=100 # MAX limit on search results per call
t_hp=60 # repeat every 60 seconds
t_it = 'Hello from the cloud. I can read your collective thoughts.'
t_ot = 'I wonder what the future holds.'
# ----------------------
# mega lists for containing stripped data from tweets
global mega_hashtags # list of hashtags 
global mega_urls #list of urls
global mega_mentions # list of mentions
mega_hashtags=[]
mega_urls=[]
mega_mentions=[]
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

def loadAdminSettings ():
	global t_st_ad
	global t_sn_ad
	try:
		adminSettings = cloud_admin.objects.filter(id=2)
		t_st_ad=adminSettings[0].search_term
		t_sn_ad=adminSettings[0].tweet_num
	except Exception as e:
		t_st_ad=t_st
		t_sn_ad=t_sn
	return (t_st_ad,t_sn_ad)

def tweet_admin(request):
	sendText="<div><h1>Cloud Tweetenstein</h1></p>"
	
	try:
		init=cloud_admin.objects.filter(id=0)
		sendText+='<p>Currently pondering the collected thoughts within tweets grouped with the term: "'
		init_ct = init.count()
		try: 
			sendText+=str(init[0].search_term)+'"</p>'
		except Exception as e:
			sendText+='Brainache caused by: "'+str(e)+'."'
	except:
		sendText+="<p>Oh, nothing created yet...</p>"
		init=cloud_admin(id=0,search_term='pug', tweet_num='100', harvest_period='60', intro_text='I am loaded', sub_text='That is not a euphemism')
		init.save()
		sendText+='<p>Now saved default sttings in line, id=0)'
	responseT = HttpResponse(sendText)
	return responseT

def weight_items(ww):
	global count_items # declares a container object to return a list in 
	count_items=[]
	#test_list=[]
	try: # need this in case list argument is borked . Also .index() would throw an error if the list was empty
		u=len(ww) # get length of list
		for l in range (0,u): # for all items in list object, increment through index values from 0 to length of list
			m=ww[l] # value of item
			ll=ww.count(m) # count of occurrances of this value in whole list
			li=ww.index(ww[l]) # "position" index value of this specific instance of the value
			if l==li: # if value of this item's index is same as index of first occurence (to create just one item in new list per distinct value)
				count_items.append(m) # ( add value of this one)
				count_items.append(str(ll)) # (add count of occurrences of this value)
	except Exception as e:
		count_items=[e] # if it fails, send the error message instead 
	return count_items# return count_items

def sort_pairs(tt):
	global sorted_items 
	sorted_items=[]
	return 'flip' # this function is NOT YET FINISHED


def saveTweetId(tid):
	global lt_stext
	global yyy
	try:
		t_id=lt_st(lt_id=tid, position=0, id=10)
		t_id.save(force_update=True)
		lt_stext="tweet id saved successfully from saveTweetId()"
		#--
		try:
			tweets = lt_st.objects.filter(id=10)
			yyy=tweets[0].lt_id
			lt_stext+=' and id ='+str(tweets[0].id)+' and lt_id ='+str(tweets[0].lt_id)+'<br />'
		except Exception as e:
			#lt_stext='Successfully retrieved tweet_id as string from lt_st.objects.all()[:1]'
			lt_stext+='nope failed get lats tweet coz : '+str(e)
			return (lt_stext)
		#--
		return lt_stext
	except Exception as e:
		lt_stext="tweet id not saved from saveTweetId() with error: "+str(e)
		return lt_stext

	# temp_tweet = lastTweetId.objects.filter(id=0)
	# str(tweets[0].last_tweet_id)

def getLastTweetId():
	global lt_rtext
	lt_rtext="default inside getLastTweetId || "
	global ttt
	ttt='ttt not set'
	try:
		tweets = lt_st.objects.filter(id=10)
		ttt=tweets[0].lt_id
		try:
			ttt+=' and id ='+str(tweets[0].id)
		except Exception as e:
			ttt+='nope failed get last tweet coz : '+str(e)
			lt_rtext+='Successfully retrieved tweet_id as string from lt_st.objects.all()[:1]<br />'
		return (lt_rtext,ttt)
	except Exception as e:
		lt_rtext='Failed via getLastTweetId() using lt_st model'+ str(e)+'<br />'
		return lt_rtext 


def last (request):
	global sendTextL
	ra=randint(0,12000)
	sendTextL="default trace text <br />"
	# try:
	# 	tweets = lastTweetId(last_tweet_id =ra)
	# 	tweets.save()
	# 	sendTextL+='last tweet model (test)created<br />'
	# except Exception as e:
	# 	sendTextL+='last tweet model (test) failed :(<br />'
	try:
		getLastTweetId()
		sendTextL+=lt_rtext+'|| -- success. tweet[xxx].id =||'+str(ttt) +'<br />'
	except Exception as e:
		sendTextL+='retrieved using getLastTweetId - fail.||'+' lt_rtext = '+lt_rtext+' || error = '+str(e)+'<br />'
	
	tweets = lt_st.objects.all()
	t_ct=tweets.count()
	t_last=tweets[t_ct-1].lt_id
	global tt
	tt=tweets.count()
	#
	sendTextL+='<br />number of stored tweets in test = '+str(tt-1)+"<br />"
	#sendTextL+=str(tweets)
	try:
		sendTextL+='Most recent value via t_last = #'+str(t_last)+'<br />'
	except Exception as e:
		sendTextL+='last tweet get failed <br />'+str(e)+'<br />'
	try:
		for e in range (0,tt-1):
			sendTextL+='tweet '+str(e)+' = '+str(tweets[e].lt_id)+' tweet id = '+str(tweets[e].id)+'<br />'
	except Exception as e:
		sendTextL+='failed to extract tweets using "for" loop'+str(e)+'<br />'
	
	last_response = HttpResponse(sendTextL)
	return last_response

def home(request):
	times = int(os.environ.get('TIMES',3))
	homeText='<html><head><title>Cloudenstein</title></head><body><h1>Hello Home World</h1></body></html>'
	loadAdminSettings ()
	t_st=t_st_ad
	t_sn=t_sn_ad
	search_tweets(t_st,t_sn)

	# try:
	# 	lass = lt(lt_id=laztwt,position=0)
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

def api (request):
	cont=100	
	get_stuff = lt_st.objects.all()[:cont]
	global gt
	gt=get_stuff.count()
	global api_text
	api_text='{"metadata":{"record_count":'+str(gt)+'},"responses":['
	try:
		for e in range (0,gt-1):
			api_text+='{"id":"'+str(get_stuff[e].id)+'","tweet_id":"'+str(get_stuff[e].lt_id)+'"}'
			if e<gt-1:
				api_text+=','
		api_text+="]}"
	except Exception as e:
		api_text='failed to respond - Returned error: '+str(e)
	api_response = HttpResponse(api_text)
	return api_response
	

def db(request):

	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})

def cloudenstein (request):
	return render (request, 'face-off.html')

def oculus (request):
	return render (request, 'oculus.html')



# ---------------search_tweets is from older Tweetenstein - to be modded ------------------
# ----------------------------------------------------------------------------------------
	responsetext="default"
def search_tweets (term,count) : # params: term= 'what to search for' type = 'how to search' Count = 'number of tweets' (max 100)
	global responsetext
	# 1: Get id of last tweet stored (to prevent saving multiple times)
	# 
	# try:
	# 	lass = lt(lt_id=int(tweet_id),position=0)
	# 	lass.save()
	# 	responsetext+='<br />tweet just saved = '+str(tweet_id)
	# except Exception as e:
	# 	responsetext+='tweetsT save failed'+str(tweet_id)
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
	search_url=str(search_url_root+term+'&count='+str(count)) # create the full search url from search term and admin setting for number of results
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
				global laztwt
				laztwt=tweet_id
				if (x==0):
					try:
						saveTweetId(tweet_id)
						responsetext+=lt_stext
					except Exception as e:
						responsetext+='Failed at saveTweetId() string because of error: '+str(e)+'<br /><br />'
					responsetext+='<h1>Results for search on term: '+term_raw+'</h1><p>'+str(c)+' tweets returned. Most recent tweet received has status id: '+str(tweet_id)+'</p>'
				name = js['statuses'][x]['user']['name']
				avatar = js['statuses'][x]['user']['profile_image_url']
				user = js['statuses'][x]['user']['screen_name']
				username= '@'+user
				global hashtags
				hashtags=''
				try: # poll throuh tweet's status.entities to look for hashtags
					ht_list=js['statuses'][x]['entities']['hashtags']
					global ht_len
					ht_len=len(ht_list)
					for xx in range(0,ht_len):
						ht_list_txt=js['statuses'][x]['entities']['hashtags'][xx]['text']
						# some code to add to hashtag list, checking for existing and counting if needed
						mega_hashtags.append(ht_list_txt)
						hashtags+='#'+ht_list_txt
						if (ht_len-xx)>0:
							hashtags+=','
				except Exception as e:
					hashtags='failed to retrieve hashtags because: '+str(e)
				global urls
				urls=''
				try: # poll throuh tweet's status.entities to look for urls
					url_list=js['statuses'][x]['entities']['urls']
					global url_len
					url_len=len(url_list)
					for xu in range(0,url_len):
						url_d_txt=js['statuses'][x]['entities']['urls'][xu]['display_url']
						url_e_txt=js['statuses'][x]['entities']['urls'][xu]['expanded_url']
						url_list_txt='<a href="'+url_e_txt+'">'+url_d_txt+'</a>'
						mega_urls.append(url_list_txt)
						urls+=url_list_txt
						if (ht_len-xu)>0:
							urls+=','
				except Exception as e:
					urls='failed to retrieve urls because: '+str(e)
				mentions=''
				try: # poll through tweet's status.entities to look for mentions
					men_list=js['statuses'][x]['entities']['user_mentions']
					global men_len
					men_len=len(men_list)
					for xm in range(0,men_len):
						men_n_txt=js['statuses'][x]['entities']['user_mentions'][xm]['name']
						men_sn_txt=js['statuses'][x]['entities']['user_mentions'][xm]['screen_name']
						men_list_txt=men_n_txt+': <a href="http://twitter.com/'+men_sn_txt+'">@'+men_sn_txt+'</a>'
						mega_mentions.append(men_list_txt)
						mentions+=men_list_txt
						if (men_len-xm)>0:
							mentions+=','
				except Exception as e:
					mentions='failed to retrieve mentions because: '+str(e)

				responsetext +='<p>Tweet: #'+str(x+1)+', status_id: '+ str(tweet_id)+', hashtags used: '+str(ht_len)+': '+hashtags+' urls cited: '+urls+'<br />'
				responsetext +='<img src="'+avatar+'" style="float:left;" />&nbsp<strong>'+name+'</strong>: '+username+')<br />'
				responsetext += '&nbsp'+js['statuses'][x]['text']+'"</p><hr />'
				
				
				# following line gets rid of Twitter line breaks...
				# tweet=tweet.replace("\n","")
				# tweet=tweet.replace("\"","'")
				# tweet=tweet.replace("\\","")
			except Exception as e:
				responsetext="Something broke while polling through tweets. This msg inside search_tweets > inside while loop"+str(e)+'<br />'
				return (responsetext,laztwt) 
			x=x+1
		try:
			getLastTweetId()
			responsetext+='sUCCESSFULLY retrieved last lt_id FROM getLastTweetId(). = '+ttt+'<br />'
			hts=', '.join(mega_hashtags) # .join() turns a list into a string, it gets the items and returns them separated by what's between the ''
			weight_items(mega_hashtags)
			htc=', '.join(count_items)
			weight_items(mega_urls)
			urlc=', '.join(count_items)
			weight_items(mega_mentions)
			menc=', '.join(count_items)
			sort_pairs(count_items)
			mens=', '.join(mega_mentions)
			responsetext+='All hashtags in this session were: '+hts+'<br /><hr />'
			responsetext+='All hashtags by count in this session were: '+htc+'<br /><hr />'
			responsetext+='All urls by count in this session were: '+urlc+'<br /><hr />'
			responsetext+='All mentions in this session were: '+mens+'<br /><hr />'
			responsetext+='All mentions by count in this session were: '+menc+'<br /><hr />'
		except Exception as e:
			responsetext+='Retrieved last tweet id FAILED FROM getLastTweetId()<br />'+str(e)+'<br />'
		return (responsetext, laztwt)
		# fullTweet2='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } ]}'
		# saveTweet2(fullTweet2)
		
	except Exception as e:
		responsetext="Failed called to Twitter. This msg inside search_tweets"+str(e)+'<br />'
		return (responsetext) 
	

# ------------- end search twitter -------------------------
# ---------------search_tweets is from older Tweetenstein - to be modded ------------------
# ----------------------------------------------------------------------------------------

# def retrieveLastTweet():
# 	global last_tweet_known
# 	last_tweet_known

