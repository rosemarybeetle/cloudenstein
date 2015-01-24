from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'gettingstarted.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^$', hello.views.index, name='index'),
	url(r'^db', hello.views.db, name='db'),
	url(r'^home', hello.views.home, name='home'),
	url(r'^tweetadmin',hello.views.tweet_admin, name='tweetadmin'),
	url(r'^cloudenstein/',hello.views.cloudenstein, name='cloudenstein'),
	url(r'^oculus/' ,hello.views.oculus, name='oculus'),
	url(r'^api/', hello.views.api, name='api'), 
	url(r'^hashtags/', hello.views.api, name='hashtags'), 
	url(r'^api/(?P<cont>\d{1,3})/$', hello.views.api), 
	url(r'^last', hello.views.last, name='last'),
	url(r'^admin/', include(admin.site.urls)),

)
