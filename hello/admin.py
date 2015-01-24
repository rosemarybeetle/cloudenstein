from django.contrib import admin

from .models import cloud_admin
from .models import process_settings
from .models import stop_words
from .models import tweeten
from .models import lt_st
from .models import hashtag

admin.site.register(cloud_admin)
admin.site.register(process_settings)
admin.site.register(stop_words)
admin.site.register(tweeten)
admin.site.register(lt_st)
admin.site.register(hashtag)
# Register your models here.

