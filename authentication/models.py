from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from phone_field import PhoneField
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class College(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=40)
    phone = PhoneField(blank=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True,null=True)
    college = models.ForeignKey(College,on_delete=models.SET_NULL,blank=True,null=True)
    department = models.CharField(max_length=40)
    year = models.IntegerField()
    
    
    def _str__(self):
        return self.username