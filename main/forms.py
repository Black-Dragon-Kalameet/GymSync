from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import User
from django import forms
from . import models

class EnquiryForm(forms.ModelForm):
     class Meta:
          model = models.Enquiry
          fields = ('enquirer_name', "enquirer_email", "enquiry_message")

class trainerloginform(forms.ModelForm):
     class Meta:
          model= models.trainer
          fields = ('username','password')

class trainerpform(forms.ModelForm):
     class Meta:
          model= models.trainer
          fields = ('full_name','mobile','address','is_active','detail','img')


class mealaddform(forms.ModelForm):
     class Meta:
          model = models.mealplan
          fields = ('subscriber','mealtime','meal')


class messageForm(forms.ModelForm):
    class Meta:
        model = models.messages
        fields = ['messages']