from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Overtimes(models.Model):
    date=models.DateField(unique=True)
    appointment_time=models.CharField(max_length=3)
    meetings=models.CharField(max_length=5)
    overtime=models.CharField(max_length=5)
    districts=models.CharField(max_length=5, null=True)
    user_id=models.IntegerField(null=True )   
    
    class Meta():
        ordering= ['-date']
     
class Pharmacy(models.Model):
    photo=models.ImageField(upload_to= 'images', null=True)
    name=models.CharField(max_length=30, )
    group=models.CharField(max_length=20)
    comment=models.CharField(max_length=200)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE,null=True  ) 
    en_name=models.CharField(max_length=20, null=True)
class Education(models.Model):
    url=models.URLField()
    comment=models.CharField(max_length=200)    
    last_visit=models.DateField()
    user_id=models.IntegerField(null=True ) 
    

    class Meta():
        ordering=['-last_visit']
        
        
class Usefull_info(models.Model):
    url=models.URLField()
    comment=models.CharField(max_length=200)    
    group=models.CharField(max_length=20)
    user_id=models.IntegerField(null=True ) 
            
