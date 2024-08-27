from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#Define the URL patterns for the app. The '' path maps to the 'home' view
urlpatterns =[
    path('',views.home,name='home'),
    path('pagedetail/<int:id>',views.page_detail,name='pagedetail'),
    path('faq',views.faq_list,name='faq'),
    path('enquiry',views.enquiry,name='enquiry'),


    #trainerstuff
    path('trainer/login',views.trainerlogin,name='trainerlogin'),
    path('trainer/logout/', views.trainer_logout, name='trainer_logout'),
    path('trainerdash',views.trainerdash,name='trainerdash'),
    path('trainerpayment',views.trainerpayment,name='trainerpayment'),
    path('trainprof',views.trainprof,name='trainprof')
    
    #requires subs model to be built, will circle back to it when subs model is built
    #path('trainersubs',views.trainersubs,name='trainersubs'),

]
#If DEBUG is True, serve media files (like images) during development
#by appending a route to the urlpatterns that maps MEDIA_URL to MEDIA_ROOT locally
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
