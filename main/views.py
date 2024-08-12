from django.shortcuts import render
from . import models
# Create your views here.
def home (request):
    banners = models.banners.objects.all()
    services = models.service.objects.all()[:3]
    
    return render(request,'home.html',{'banners':banners,'services':services})