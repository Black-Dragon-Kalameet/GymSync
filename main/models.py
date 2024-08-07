from django.db import models

# Create your models here.
class service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField(2)