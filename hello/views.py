import os
import time
import twitter
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
from .models import stop_words
from .models import process_settings
from .models import cloud_admin
from .models import tweeten
from .models import process_settings
from .models import hashtags
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
global responsetext # used to collect text for httpRseponse returns
responsetext='' # initialise as string
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
loop_flag=True
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
	tweetings = tweeten.objects.all()
	return render(request, 'index.html', {'tweetings': tweetings})

def visualiser (request):
	#twaatings = tweeten.objects.all()
	return render (request, 'visualiser.html')#, {'twaatings': twaatings})


def oculus (request):
	twaatings = tweeten.objects.all()
	return render (request, 'oculus.html', {'twaatings': twaatings})

def admin_clock(request):
	t1=time.time()
	t2=time.time()
	x=0
	loadAdminSettings()
	period=t_hp_ad
	textCA='elapsed'
	while x>0:
		if (t1-t2)<period:
			t1=time.time()
		else:
			t1=time.time()
			t2=time.time()
			x+=1
			textCA='elpased '+str(x)
			responsCA = HttpResponse(textCA)
			return responseCA

def db(request):
	greeting = Greeting()
	greeting.save()
	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})

def spiraliser(request):
	loadAdminSettings ()
	return render(request, 'spiraliser.html', {'period':t_hp_ad})

	

def loadAdminSettings ():
	global t_st_ad
	global t_sn_ad
	global t_hp_ad
	try:
		adminSettings = cloud_admin.objects.filter(id=2)
		t_st_ad=adminSettings[0].search_term
		t_sn_ad=adminSettings[0].tweet_num
		t_hp_ad=adminSettings[0].harvest_period
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
				count_items.append(str(m)) # ( add value of this one)
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
		global last_tweet
		last_tweet=ttt
		try:
			ttt+=' and id ='+str(tweets[0].id)
		except Exception as e:
			ttt+='nope failed get last tweet coz : '+str(e)
			lt_rtext+='Successfully retrieved tweet_id as string from lt_st.objects.all()[:1]<br />'
		return (lt_rtext,ttt,last_tweet)
	except Exception as e:
		lt_rtext='Failed via getLastTweetId() using lt_st model'+ str(e)+'<br />'
		return lt_rtext 


def last (request):
	global sendTextL
	global tt
	tt=0
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
	try:
		tweety = lt_st.objects.all()
		t_ct=tweety.count()
		t_last=tweety[t_ct-1].lt_id
		tt=tweety.count()
	
	except Exception as e:
		sendTextL+='error creating tweety'+str(e)
	#
	sendTextL+='<br />number of stored tweets in test = '+str(tt-1)+"<br />"
	#sendTextL+=str(tweets)
	try:
		sendTextL+='Most recent value via t_last = #'+str(t_last)+'<br />'
	except Exception as e:
		sendTextL+='last tweet get failed <br />'+str(e)+'<br />'
	try:
		for e in range (0,tt-1):
			sendTextL+='tweet '+str(e)+' = '+str(tweety[e].lt_id)+' tweet id = '+str(tweety[e].id)+'<br />'
	except Exception as e:
		sendTextL+='failed to extract tweets using "for" loop'+str(e)+'<br />'
	
	last_response = HttpResponse(sendTextL)
	return last_response

	# ------------------
def keeplooping():  # define the loop and what it executes (rate is set by loaded setting: 'harvestPeriod' 
	harvestPeriod=60
	Timer(int(harvestPeriod), keeplooping).start()
	Timer(int(harvestPeriod)*.3, home).start()

	# ------------------

# def home(request):
# 	try:
# 		homeText='<html><head><title>Home</title></head><body><h1>Hello World, Home</h1>'
# 		search_tweets()	
# 		homeText+=responsetext+'</body></html>'
# 		home_response = HttpResponse(homeText)
# 		return home_response
# 	except Exception as e:
# 		homeText=' failed in Home, because... ' + str(e)
# 	# homeText='hellow home world'
# 	# home_response = HttpResponse(homeText)
# 		return home_response
 #----------------------
def home(request):
	# times = int(os.environ.get('TIMES',3))
	homeText='<html><head><title>Cloudenstein</title></head><body><h1>Hello Home World</h1>'
	loadAdminSettings ()
	t_st=t_st_ad
	t_sn=t_sn_ad
	#responsetext=''
	
	search_tweets(t_st,t_sn)
	# try:
	# 	lass = lt(lt_id=laztwt,position=0)
	# 	lass.save()
	# 	responsetext+='<br />tweet just saved = '+str(laztwt)
	# except Exception as e:
	# 	responsetext+='lass save failed'+str(laztwt)
	
	homeText+=responsetext+'</body></html>'
	
	home_response = HttpResponse(homeText)
	return home_response
 #----------------------

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
			if ((gt-2)-e)>0:
				api_text+=','
		api_text+="]}"
	except Exception as e:
		api_text='failed to respond - Returned error: '+str(e)
	api_response = HttpResponse(api_text)
	return api_response
def send_tweet(tw_st):
	my_auth = twitter.OAuth(twit_api_access_token,twit_api_access_secret,twit_api_key,twit_api_secret)
	twit = twitter.Twitter(auth=my_auth)
	twit.statuses.update(status=tw_st)

def ht_c (request): # api end point for counted + weighted tags
	loadAdminSettings()
	ss=0
	try:
		ss=randint(1,1000)
		tweet_st_text=str(ss)+'troika test spout_tweet() @rbeetlelabs - Cloudenstein: http://cloudenstein.rosemarybeetle.org'
		send_tweet(tweet_st_text)
	except Exception as e:
		bo='tweeting not playing: '+str(e)
	global htc_ary
	htc_ary=[]
	get_stuff = hashtags.objects.all()#[:cont]
	global hts_count
	hts_count=get_stuff.count()
	try:
		htc_text='<html><head><title>ht_c</title></head><body><p>'+bo+'{"metadata":{"record_count":'+str(hts_count)+'"},"responses":['
	except:
		htc_text='<html><head><title>ht_c</title></head><body><p>{"metadata":{"record_count":'+str(hts_count)+'"},"responses":['
	try:
		tag_str_all=''
		for t in range (0,hts_count-1): # make a comma seaparted list of all the stored hashtags
			tag_str=str(get_stuff[t].ht_term) # get next tag 
			if ((hts_count-2)-t)>0: # add a comma as long as not the last value
				tag_str+=','
			tag_str_all+=' '+tag_str
			htc_ary.append(tag_str)
		hts=', '.join(htc_ary)
		weight_items(tag_str_all) # call the weighting function
		xxx=count_items
		weight_items(hts)
		yyy=count_items
		htc_text+=str(xxx)+ ' All = ' +str(tag_str_all) + ' and also'+ str(yyy)
		htc_text+='<br /></body></html>'
		#htc_text+='{"tag":"'+str(get_stuff[t].ht_term)+'","Search term":"'+str(get_stuff[t].ht_st)+'"}'
	except Exception as e:
		htc_text+=str(e)
	htc_response = HttpResponse(htc_text)
	return htc_response

	
	
def ht (request):
	#cont=100
	loadAdminSettings()
	get_stuff = hashtags.objects.all()#[:cont]
	global g_tags
	g_tags=get_stuff.count()
	global api_text_ht
	api_text_ht='{"metadata":{"record_count":'+str(g_tags)+'"},"responses":['
	try:
		for t in range (0,g_tags-1):
			api_text_ht+='{"tag":"'+str(get_stuff[t].ht_term)+'","Search term":"'+str(get_stuff[t].ht_st)+'"}'
			if ((g_tags-2)-t)>0:
				api_text_ht+=','
		api_text_ht+="]}"
	except Exception as e:
		api_text_ht='failed to respond - Returned error: '+str(e)
	api_response_ht = HttpResponse(api_text_ht)
	return api_response_ht



def cloudenstein (request):
	return render (request, 'face-off.html')


#----------------------------------------------------------------------------------------
def search_tweets (term,count) : # params: term= 'what to search for' type = 'how to search' Count = 'number of tweets' (max 100)
	getLastTweetId()
	global responsetext
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
		j = (auth_response.text)
		js = json.loads(j)
		js_dict=js
		global js_count
		js_count=len(js_dict['statuses'])# how many tweets in thi response? - double checking that number of tweets received was same as asked for (could be less occassionally)
		c = js_count
		x=0
		while (x<c):
			try:
				tweet_id = js['statuses'][x]['id']
				global laztwt
				laztwt=tweet_id
				if (x==0):
					global temp_tweet
					temp_tweet=tweet_id
					responsetext+='<h1>Results for search on term: '+term_raw+'</h1><p>'+str(c)+' tweets returned. Most recent tweet received has status id: '+str(tweet_id)+'</p>'
				name = js['statuses'][x]['user']['name']
				avatar = js['statuses'][x]['user']['profile_image_url']
				user = js['statuses'][x]['user']['screen_name']
				username= '@'+user
				tweet_text=js['statuses'][x]['text']
				t1 =int(tweet_id)
				t2=int(last_tweet)
				try:
					if t1>t2:
						saveTweet(tweet_id,name,user,avatar,tweet_text)
						responsetext+="SUCCESS - real  RECORD CREATED<br /> t1= "+str(t1)+", t2 = "+str(t2)+'  although'+str(ff)
					else:
						responsetext+="this tweet already in database - no need to save"
				except Exception as e:
					responsetext+="FAILED - real RECORD NOT CREATED BECAUsE OF ERROR: "+str(e)+'<br />'
					# V---------------------do sub content-------------------V
				global tip_hashtags
				tip_hashtags=''
				try: # poll throuh tweet's status.entities to look for tip_hashtags
					ht_list=js['statuses'][x]['entities']['hashtags']
					global ht_len
					ht_len=len(ht_list)
					for xx in range(0,ht_len):
						ht_list_txt=js['statuses'][x]['entities']['hashtags'][xx]['text']
						# some code to add to hashtag list, checking for existing and counting if needed
						saveHashtags('#'+str(ht_list_txt))
						mega_hashtags.append(ht_list_txt)
						tip_hashtags+='#'+ht_list_txt
						if (ht_len-xx)>0:
							tip_hashtags+=','
				except Exception as e:
					tip_hashtags='failed to retrieve hashtags because: '+str(e)
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
				# ^------------------------end sub content ----------------------------^
				responsetext +='<p>Tweet: #'+str(x+1)+', status_id: '+ str(tweet_id)+', hashtags used: '+str(ht_len)+': '+tip_hashtags+' urls cited: '+urls+'<br />'
				responsetext +='<img src="'+avatar+'" style="float:left;" />&nbsp<strong>'+name+'</strong>: '+username+')<br />'
				responsetext += '&nbsp'+js['statuses'][x]['text']+'"</p><hr />'
				
				
			except Exception as e:
				responsetext+="Something broke while polling through tweets. This msg inside search_tweets > inside while loop: "+str(e)+'<br />'
				return (responsetext,laztwt) 
			x=x+1
		try:
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
		try:
			saveTweetId(temp_tweet)
			#responsetext+='text from inside saveTweetId = '+str(lt_stext)
		except Exception as e:
			responsetext+='Failed at saveTweetId() string because of error: '+str(e)+'<br /><br />'
		return (responsetext, laztwt)
		# fullTweet2='{"tweet_id": "'+str(tweet_id)+'","username": "'+str(username)+'","screen_name": "'+str(name)+'","tweet_text": "'+str(tweet)+'" } ]}'
		# saveTweet2(fullTweet2)
	except Exception as e:
		responsetext+="Failed called to Twitter. This msg inside search_tweets"+str(e)+'<br />'
		return (responsetext) 
	



def saveTweet(tweet_id,name,user,avatar,text):
	global twt_n_id
	global twt_0_id
	global ff
	ff='default'
	try:
		retrieveProcessSettings()
		tweeten_max=p_max_tweets
		tweeten_all=tweeten.objects.all() 
		tweeten_l=len(tweeten_all)# retrieve number in tweet store
		if int(tweeten_l) > int(tweeten_max) :
			#popper=tweeten.objects.all()
			tweeten_all[0].delete()
			saved_tweet=tweeten(tid=tweet_id,t_name=name,t_username=user,t_status=text,t_avatar=avatar)
			saved_tweet.save()
			ff = 'tweeten_l= '+str(tweeten_l)+'tweeten_max = '+str(tweeten_max)
			return ff
		else:
			saved_tweet=tweeten(tid=tweet_id,t_name=name,t_username=user,t_status=text,t_avatar=avatar)
			ff = 'ttttttttttttweeten_l= '+str(tweeten_l)+'tweeten_max = '+str(tweeten_max)
			saved_tweet.save()
			return ff
	except Exception as e :
		ff ='failed on : '+str(e)
		return ff # random
	
def saveHashtags(hash_list_arg):
	retrieveProcessSettings()
	hash_max=p_max_tags
	global s_ht_term
	global hh
	hh='default'
	temp_tags=hashtags.objects.all()
	hash_len=len(temp_tags)
	hh='argument received in hashtag saver . '
	s_ht_term=hash_list_arg
	uu=str(s_ht_term)
	vv=str(t_st_ad)
	if str.lower(uu)!=str.lower(vv): # stops search term hashtags being saved and swamping weighting
		if hash_len > hash_max :
			temp_tags[0].delete()
			saved_hashtag=hashtags(ht_term=s_ht_term, ht_st=t_st_ad)
			saved_hashtag.save()
			hh+='hashtag saved = '+str (s_ht_term)
		else:
			saved_hashtag=hashtags(ht_term=s_ht_term, ht_st=t_st_ad)
			saved_hashtag.save()
			hh+='hashtag savedddddddddddddd = '+str (s_ht_term)
	else:
		hh+='hastag matches search term. Not saved'
	return hh

def retrieveProcessSettings():
	global p_max_tweets
	global p_st_date
	global p_end_date
	global p_max_tags
	global p_max_mens
	global p_max_words
	global p_cnt_type
	global p_st
	p_setts=process_settings.objects.filter(id=1)
	p_max_tweets=p_setts[0].max_tweets
	p_st_date=p_setts[0].st_date
	p_end_date=p_setts[0].end_date
	p_max_tags=p_setts[0].max_tags
	p_max_mens=p_setts[0].max_mens
	p_max_words=p_setts[0].max_words
	p_cnt_type=p_setts[0].cnt_type
	p_st=p_setts[0].st
	return(p_max_tweets,p_st_date, p_end_date,p_max_tags,p_max_mens,p_max_words,p_cnt_type,p_st )

def create_batch():
	test=0
	# pseudo code 
	# search twitter to creat new temp_batch of tweets, based on cloud_admin() settings
	# retrieve most recent saved tweet id using functionx()
	# for each tweet in temp_batch:
	# 	if tweet_id > last_saved_tweet_id
	# 	save tweet() which means:
	# 		if currebatch.size > batch_limit from process_setting()
	# 		delete oldest tweet in batch
	# 		add new tweet to end 
	# 	process tweet()
	# 		harvest_usernames()
	# 		harvest_urls
	# 		harvest_hashtags
	# 	increment batch.count
	# once all processed, update last_saved_tweet_id 

# -
