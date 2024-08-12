from django.contrib import admin
from . import models

# Register your models here.
#-----

class banneradmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')  
admin.site.register(models.banners,banneradmin)

class serviceadmin(admin.ModelAdmin):
    list_display=('title','image_tag')  
admin.site.register(models.service,serviceadmin)
