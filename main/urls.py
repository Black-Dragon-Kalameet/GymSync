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
    path('trainerlogin', views.trainerlogin, name='trainerlogin'),
    path('trainerlogout', views.trainerlogout, name='trainerlogout'),
    path('trainer_dashboard', views.trainer_dashboard, name='trainer_dashboard'),
    path('trainer_profile', views.trainer_profile, name='trainer_profile'),
    path('trainer_payments', views.trainer_payments, name='trainer_payments'),
    path('mealplan',views.mealplan,name='mealplan'),
    path('trainer_change_password', views.trainer_change_password, name='trainer_change_password'),
    path('trainer_notifs', views.trainer_notifs, name='trainer_notifs'),
    path('trainer_subscribers', views.trainer_subscribers, name='trainer_subscribers'),

    # Notifications
    path('notifs', views.notifs, name='notifs'),
    path('get_notifs', views.get_notifs, name='get_notifs'),
    path('mark_read_notif', views.mark_read_notif, name='mark_read_notif'),

    # Messages
    path('messages', views.trainer_msgs, name='messages'),

]
#If DEBUG is True, serve media files (like images) during development
#by appending a route to the urlpatterns that maps MEDIA_URL to MEDIA_ROOT locally
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
