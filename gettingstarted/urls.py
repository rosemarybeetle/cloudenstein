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
	url(r'^tweet_admin',hello.views.tweet_admin, name='tweet_admin'),
	url(r'^last',hello.views.last, name='last'),
	url(r'^admin/', include(admin.site.urls)),

)
