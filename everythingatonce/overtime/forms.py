from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from .models import Overtimes, Pharmacy, Education, Usefull_info


class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model=User
        fields= ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user=super(NewUserForm, self).save(commit=False)
        user.email=self.cleaned_data['email']   
        if commit:
            user.save()
        return user    


class OvertimesInfo(forms.Form):
    date=forms.DateField()
    appointment_time=forms.CharField(max_length=3)
    meetings=forms.IntegerField()
    overtime=forms.CharField(max_length=5)
    
    
class PharmacyImageForm(forms.ModelForm):
    class Meta:
        model=Pharmacy
        fields=['name', 'photo', 'comment', 'group']
            
    
    