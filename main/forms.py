from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import User
from django import forms
from . import models

# Enquiry Form
class EnquiryForm(forms.ModelForm):
     class Meta:
          model = models.Enquiry
          fields = ('enquirer_name', "enquirer_email", "enquiry_message")


# User registration form with the below fields
class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


# Edit user's profile
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


# Trainer Login form
class trainerloginform(forms.ModelForm):
     class Meta:
          model= models.trainer
          fields = ('username','password')


# Trainer Profile Form
class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model = models.Trainer
        fields = ('full_name', 'mobile', 'address', 'img', 'details', 'facebook', 'instagram', 'twitter', 'youtube', 'blog')


# Trainer - Change Password
class TrainerChangePasswordForm(forms.ModelForm):
    new_password = forms.CharField(max_length=50, required=True)