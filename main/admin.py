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

class FaqAdmin(admin.ModelAdmin):
    list_display=('question',)  
admin.site.register(models.Faq,FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('enquirer_name', "enquirer_email", "enquiry_message", "enquiry_dateAndTime")  
admin.site.register(models.Enquiry,EnquiryAdmin)
#trainermodel, this adds the colomns in admin panel and adds the trainers tab itself, list editable makes it so that u can uncheck and check the the is_active pararmeter 
class traineradmin(admin.ModelAdmin):
    list_editable = ('is_active',)
    list_display=('full_name','mobile','is_active','image_tag')
admin.site.register(models.trainer,traineradmin)

class mealadmin(admin.ModelAdmin):
    list_display=('subscriber','mealtime','meal')
admin.site.register(models.mealplan,mealadmin)

class messagesadmin(admin.ModelAdmin):
    list_display=('trainer','messages')
    
admin.site.register(models.messages,messagesadmin)