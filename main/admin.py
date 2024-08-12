from django.contrib import admin
from . import models

# Register your models here.
#Adding website parts to the admin panel side

#display the 'alt_text' and the image thumbnail ('image_tag') for each banner
class banneradmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')  
admin.site.register(models.banners,banneradmin)

#display the 'title' and the image thumbnail ('image_tag') for each service
class serviceadmin(admin.ModelAdmin):
    list_display=('title','image_tag')  
admin.site.register(models.service,serviceadmin)

class pageadmin(admin.ModelAdmin):
    list_display=('title',)  
admin.site.register(models.Page,pageadmin)