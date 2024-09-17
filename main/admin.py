from django.contrib import admin
from . import models

# Register your models here.
#Adding website parts to the admin panel side

#display the 'alt_text' and the image thumbnail ('image_tag') for each banner
class Banneradmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')  
admin.site.register(models.banners,Banneradmin)

#display the 'title' and the image thumbnail ('image_tag') for each service
class Serviceadmin(admin.ModelAdmin):
    list_display=('title','image_tag')  
admin.site.register(models.service,Serviceadmin)

class Pageadmin(admin.ModelAdmin):
    list_display=('title',)  
admin.site.register(models.Page,Pageadmin)

class FaqAdmin(admin.ModelAdmin):
    list_display=('question',)  
admin.site.register(models.Faq,FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('enquirer_name', "enquirer_email", "enquiry_message", "enquiry_dateAndTime")  
admin.site.register(models.Enquiry,EnquiryAdmin)
#trainermodel, this adds the colomns in admin panel and adds the trainers tab itself, list editable makes it so that u can uncheck and check the the is_active pararmeter 
class Traineradmin(admin.ModelAdmin):
    list_editable = ('is_active',)
    list_display=('full_name','mobile','is_active','image_tag')
admin.site.register(models.trainer,Traineradmin)

class Mealadmin(admin.ModelAdmin):
    list_display=('subscriber','mealtime','meal')
admin.site.register(models.mealplan,Mealadmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display=('title', 'image_tag')  
admin.site.register(models.Gallery,GalleryAdmin)

class GalleryImage(admin.ModelAdmin):
    list_display=('alt_text', 'image_tag')  
admin.site.register(models.GalleryImage,GalleryImage)