from django.shortcuts import render, redirect
from .forms import NewUserForm, OvertimesInfo, PharmacyImageForm
from django.contrib.auth import login
from django.views import generic
from django.db.models import Sum
from .models import Overtimes, Pharmacy, Education, Usefull_info
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.models import User
from django.urls import reverse
from .parsing0 import get_image
import os
from PIL import Image
import shutil
from django.core.files.base import ContentFile
from io import BytesIO
from uuid import uuid4
from django.core.files import File
# Create your views here.



def index(request):
    
    
    days=Overtimes.objects.filter(user_id=4).count()
    
    overtimes=Overtimes.objects.filter(user_id=4).aggregate(Sum('overtime'))
    l=overtimes['overtime__sum']
    if l==None:
        l=0
       
    print(overtimes)
    print(l)
    
   
    
    
    return render(request, 'index.html', context={'days':days, 'l':l})


def find_overtime(app, distr, meets):
    return round(-((7.5-float(app))*float(distr)-float(meets)/3),1)


def register_request(request):
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "Новый страдалец")
            return redirect('overtimes')  
        messages.error(request, "нормальные данные введи")
    form= NewUserForm()
    return render(request=request, template_name='overtime/register.html', context={"register_form":form})        
 
class OvertimesListView(generic.ListView):
    model=Overtimes
    
    
    def get_queryset(self):
        return Overtimes.objects.filter(user_id=self.request.user.id)
    
@login_required   
def add_overtimes(request):
    if request.method == 'POST':
        user=request.user
        user_id=user.id
        
        
        
        overtimes=Overtimes()
        overtimes.date=request.POST.get('date')
        overtimes.appointment_time=request.POST.get('appointment_time')
        overtimes.meetings=request.POST.get('meetings')
        overtimes.districts=request.POST.get('districts')
        overtimes.overtime=find_overtime(overtimes.appointment_time,overtimes.districts, overtimes.meetings)
        overtimes.user_id=user_id
        overtimes.save()
        return redirect('overtimes')  
    return render(request, 'overtime/add_overtimes.html')   
@login_required  
def edit(request, id):
    try:
        overtime = Overtimes.objects.get(id=id)
 
        if request.method == "POST":
            
            overtime.date = request.POST.get("date")
            overtime.appointment_time = request.POST.get("appointment_time")
            overtime.districts=request.POST.get('districts')
            overtime.meetings=request.POST.get('meetings')
            overtime.overtime=find_overtime(overtime.appointment_time,overtime.districts, overtime.meetings)
            
            
            
            overtime.save()
            return redirect('overtimes') 
        else:
            return render(request, "overtime/edit.html")
    except overtime.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
@login_required  
def delete(request, id):
    try:
        overtime = Overtimes.objects.get(id=id)
        overtime.delete()
        return redirect('overtimes')   
    except overtime.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")    
    
    
class PharmacyListView(generic.ListView):
    model=Pharmacy
    
    def get_queryset(self):
        group=self.request.GET.get('filter', '')
        if not group:
            return self.model.objects.all()
        return self.model.objects.filter(group=group)
    
    
    
        
    
@login_required   
def add_pharmacy_m(request):
    if request.method == 'POST':
        form=PharmacyImageForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('pharmacy')   
    else:
        form=PharmacyImageForm()    
        
    return render(request, 'overtime/add_pharmacy_m.html', {'form':form})       

@login_required
def add_pharmacy(request):
    
    if request.method == 'POST':
        
        name=request.POST.get('name')
        #user=request.user
        #user_id=user.id
        version=get_image(name)
        
        
        
        
        return render(request, 'overtime/add_pharmacy.html', {'name':name, 'version':version})
        
       
        
        
        
    return render(request, 'overtime/add_pharmacy.html') 


def add_pharmacy_a(request):
        if request.method == 'POST':
             pharmacy=Pharmacy()
             pharmacy.name=request.POST.get('namePh')
             pharmacy.group=request.POST.get('group')
             pharmacy.comment=request.POST.get('comment')
             im=Image.open(f'/Users/admin/karpovfamily/everythingatonce/media/images/000001.jpg')
       
             blob=BytesIO()
             im.save(blob, 'JPEG')
             pharmacy.photo.save(f'{pharmacy.name}.jpg', File(blob), save=False)
        
        
        
        
        
             pharmacy.save()
             return redirect('pharmacy')   
        return render(request, 'overtime/add_pharmacy_a.html')     

@login_required  
def delete_pharmacy(request, id):
    try:
        pharmacy = Pharmacy.objects.get(id=id)
        pharmacy.delete()
        return redirect('pharmacy')   
    except overtime.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>") 











class EducationListView(generic.ListView):
    model=Education
    
    
    
class Usefull_infoListView(generic.ListView):
    model=Usefull_info
                