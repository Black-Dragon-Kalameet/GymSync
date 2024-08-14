from django.shortcuts import render
from . import models
from . import forms
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

# Enquiry
def enquiry(request):
    message = ''
    if request.method == 'POST':
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Your enquiry has been sent successfully.'
    form = forms.EnquiryForm
    return render(request,'enquiry.html',{'form':form, 'message': message})
