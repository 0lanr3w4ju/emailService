from django.db import models

# Create your models here.

class ContactUsModel(models.Model):

    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=False)
    email = models.CharField(max_length=200,blank=False)
    phone_no = models.CharField(max_length=50, blank=False)
    service_loc = models.CharField(max_length=100,blank=False)
    available_date = models.DateField(blank=False)

    
