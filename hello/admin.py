from django.contrib import admin

from .models import cloud_admin
from .models import process_settings
from .models import stop_words
from .models import tweeter

admin.site.register(cloud_admin)
admin.site.register(process_settings)
admin.site.register(stop_words)
admin.site.register(tweeter)
# Register your models here.

