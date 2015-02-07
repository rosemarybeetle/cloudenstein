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
	url(r'^visualiser', hello.views.visualiser, name='visualiser'),
	url(r'^spiraliser', hello.views.spiraliser, name='spiraliser'),
	url(r'^home', hello.views.home, name='home'),
	url(r'^admin_clock', hello.views.admin_clock, name='admin_clock'),
	url(r'^tweetadmin',hello.views.tweet_admin, name='tweetadmin'),
	url(r'^cloudenstein/',hello.views.cloudenstein, name='cloudenstein'),
	url(r'^twt/',hello.views.twt, name='twt'),
	url(r'^oculus/' ,hello.views.oculus, name='oculus'),
	url(r'^api/$', hello.views.api, name='api'), 
	url(r'^api/(?P<coont>\d+)/$', hello.views.api), 
	url(r'^ht/', hello.views.ht, name='api_ht'), 
	url(r'^htc/', hello.views.ht_c, name='api_htc'), 
	url(r'^last', hello.views.last, name='last'),
	url(r'^admin/', include(admin.site.urls)),

)
