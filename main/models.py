from django.db import models
from django.utils.html import mark_safe 

#BANNERS Data
class banners(models.Model):
    img=models.ImageField(upload_to="banners/")
    alt_text=models.CharField(max_length=150)
    #Names images after their alt text
    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
    # Returns an HTML <img> tag to display the product's image in the admin interface
    # The image is displayed as a thumbnail with a width of 80 pixels.
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))

# Pages for Privacy and Terms Data
class Page(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()

    def __str__(self):
        return self.title
        
# FAQ Data
class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
        
# Services Data
class service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img=models.ImageField(upload_to="services/",null=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))
    
# Enquiry Form Data
class Enquiry(models.Model):
    enquirer_name = models.CharField(max_length=150)
    enquirer_email = models.CharField(max_length=150)
    enquiry_message = models.TextField()
    enquiry_dateAndTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.enquirer_name
        