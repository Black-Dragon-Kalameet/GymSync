from django.shortcuts import render,redirect
from django.contrib.auth import logout
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
    # Save the posted enquiry and show a message after posting an enquiry
    if request.method == 'POST':
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Your enquiry has been sent successfully.'
            
    form = forms.EnquiryForm
    return render(request,'enquiry.html',{'form':form, 'message': message})

# trainers
def trainerlogin(request):
    message = ''
    
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        trainer = models.trainer.objects.filter(username=username,password=password).count()
        if trainer > 0:
            request.session['trainerlogin'] = True
            print("User authenticated:", request.user.is_authenticated)
            print("Trainer login session:", request.session.get('trainerLogin'))
            #return redirect('/trainerdash')
        else:
            message ='wrong'
            
    form = forms.trainerloginform
    return render(request,'trainerlogin.html',{'form':form, 'message': message})



def trainer_logout(request):
    # Clear the trainerLogin session variable
    request.session.pop('trainerLogin', None)
    # Log out the user
    logout(request)
    # Redirect to the home page or another page
    return redirect('/')