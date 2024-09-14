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

        try:
            trainer = models.trainer.objects.get(username=username,password=password)
            request.session['trainerlogin'] = True
            request.session['trainerid'] = trainer.id
            print("User authenticated:", request.user.is_authenticated)
            print("Trainer login session:", request.session.get('trainerLogin'))
            return redirect('/trainerdash')
        
        except models.trainer.DoesNotExist:
            message ='wrong'

     
  
            
    form = forms.trainerloginform
    return render(request,'trainer/trainerlogin.html',{'form':form, 'message': message})



def trainer_logout(request):
    # Clear the trainerLogin session variable
    request.session.pop('trainerLogin', None)
    # Log out the user
    logout(request)
    # Redirect to the home page or another page
    return redirect('/')

def trainerdash(request):
    return render(request,'trainer/dashboard.html')

def trainerpayment(request):
    #trainer = models.trainer.objects.get(pk=request.session['trainerid'])
    trainerpaym = [{'amount':120, 'date':'1/1/2024'},
                   {'amount':150, 'date':'1/2/2024'}
                   
                   ]
    #once model is bult for payment, retrieve here the payments from the database


    return render(request, 'trainerpayment.html',{'trainerpaym':trainerpaym})

def trainprof(request):
    msg =None
    trainid =  request.session['trainerid']
    traineri = models.trainer.objects.get(id=trainid)
    if request.method == 'POST':
       form = forms.trainerpform(request.POST,request.FILES,instance=traineri)
       if form.is_valid:
           form.save()
           msg ='profile updated'
    
    form = forms.trainerpform(instance=traineri)
    return render(request,'trainer/profile.html',{'form':form,'msg':msg})

def mealplan(request):

    trainid =  request.session['trainerid']
    trainer = models.trainer.objects.get(id=trainid)
    mealplan = trainer.mealplans.all()


    return render(request,'mealplan.html',{'mealplan':mealplan})


# Assigned subscribers to the trainer
def trainer_subscribers(request):
    trainer = models.Trainer.objects.get(pk=request.session['trainerid'])
    trainer_subs = models.AssignSubscriber.objects.filter(trainer=trainer).order_by('-id')

    return render(request, 'trainer/trainer_subscribers.html', {'trainer_subs' : trainer_subs})


# Trainer - Change Password
def trainer_change_password(request):
    msg = None

    if request.method =='POST':
        new_password = request.POST['new_password']
        update_response = models.Trainer.objects.filter(pk=request.session['trainerid']).update(password=new_password)

        if update_response:
            msg = "Password Changed Successfully"
            del request.session['trainerid']
            return redirect('/trainerlogin')
        else:
            msg = "Password Change Failed"

    form = forms.TrainerChangePasswordForm

    return render(request, 'trainer/trainer_change_password.html', {'form' : form, 'msg': msg})


# Trainer Notifications
def trainer_notifs(request):
    data = models.TrainerNotification.objects.all().order_by('-id')

    return render(request, 'trainer/notifs.html', {'notifs' : data})


# Trainer Messages
def trainer_msgs(request):
    data = models.TrainerMessage.objects.all().order_by('-id')

    return render(request, 'trainer/messages.html', {'msgs' : data})