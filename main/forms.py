from django import forms
from . import models

class EnquiryForm(forms.ModelForm):
     class Meta:
          model = models.Enquiry
          fields = ('enquirer_name', "enquirer_email", "enquiry_message")