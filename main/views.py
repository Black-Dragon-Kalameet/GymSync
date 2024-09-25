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
    return render(request,'trainerlogin.html',{'form':form, 'message': message})



def trainer_logout(request):
    # Clear the trainerLogin session variable
    request.session.pop('trainerLogin', None)
    # Log out the user
    logout(request)
    # Redirect to the home page or another page
    return redirect('/')

def trainerdash(request):
    return render(request,'trainerdash.html')

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
    return render(request,'trainprof.html',{'form':form,'msg':msg})

def mealplan(request):

    trainid =  request.session['trainerid']
    trainer = models.trainer.objects.get(id=trainid)
    mealplan = trainer.mealplans.all()


    return render(request,'mealplan.html',{'mealplan':mealplan})

def mealadd(request):
    msg = None
    trainid = request.session.get('trainerid')

    if request.method == 'POST':
        form = forms.mealaddform(request.POST, request.FILES)
        if form.is_valid():
            mealplan = form.save(commit=False)
            mealplan.trainer_id =trainid
            mealplan.save()
            msg = 'Meal added successfully'
            return redirect('mealplan') 
    
    form = forms.mealaddform()  
    return render(request, 'mealadd.html', {'form': form, 'msg': msg})


def trainer_messages(request):
    if not request.session.get('trainerlogin'):
        return redirect('trainerlogin')

    trainer_id = request.session.get('trainerid')
    
    # Ensure 'messages' is used correctly here
    trainer_messages = models.messages.objects.filter(trainer_id=trainer_id).order_by('-id') if trainer_id else []

    if request.method == 'POST':
        form = forms.messageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.trainer_id = trainer_id
            new_message.save()
            return redirect('trainer_messages')
    else:
        form = forms.messageForm()

    context = {
        'messages': trainer_messages,  # Pass the messages for the template
        'form': form
    }

    return render(request, 'trainer_messages.html', context)