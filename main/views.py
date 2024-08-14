from django.shortcuts import render
from . import models
# Create your views here.
def home (request):
    banners = models.banners.objects.all()
    services = models.service.objects.all()[:3]
    return render(request,'home.html',{'banners':banners,'services':services})

#PageDetail
def page_detail(request, id):
    page = models.Page.objects.get(id = id)
    return render(request,'page.html',{'page':page})

# FAQ
def faq_list(request):
    faqs = models.Faq.objects.all
    return render(request,'faq.html',{'faqs':faqs})
