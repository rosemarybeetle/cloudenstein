from django.contrib import admin

from .models import cloud_admin
from .models import process_settings
from .models import stop_words

admin.site.register(cloud_admin)
admin.site.register(process_settings)
admin.site.register(stop_words)
# Register your models here.

