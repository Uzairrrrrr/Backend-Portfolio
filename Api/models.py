from django.db import models

# Create your models here.
class About(models.Model):
    content1 = models.CharField(max_length=2000)
    content2 = models.CharField(max_length=2000)
    content3 = models.CharField(max_length=2000)
    content4 = models.CharField(max_length=2000)

class Work(models.Model):
    date = models.DateField(blank=True, null=True)
    heading = models.CharField(max_length=100, blank=True, null=True)
    post = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=2000)

class Education(models.Model):
    date = models.DateField(blank=True, null=True)
    heading = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=2000)

class Services(models.Model):
    heading = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)

class WorkDone(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='static/images/',null=True,blank=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=100)

class Testimonials(models.Model):
    content = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='static/images/')
    name = models.CharField(max_length=50, blank=True, null=True)
    post = models.CharField(max_length=100, blank=True, null=True)  
      
