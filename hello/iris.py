def make_iris (term,count) : # params: term= 'what to search for' type = 'how to search' Count = 'number of tweets' (max 100)
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
	
