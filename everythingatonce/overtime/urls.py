from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_request, name= 'register'),
    path('overtimes/', views.OvertimesListView.as_view(), name='overtimes'),
    path('add_overtimes/', views.add_overtimes, name='add_overtimes'),
    path("overtimes/edit/<int:id>/", views.edit),
    path("overtimes/delete/<int:id>/", views.delete),
    path('pharmacy/', views.PharmacyListView.as_view(), name='pharmacy'),
    path('education/', views.EducationListView.as_view(), name='education'),
    path('usefull_info/', views.Usefull_infoListView.as_view(), name='usefull_info'),
    path('add_pharmacy/', views.add_pharmacy, name='add_pharmacy'),
    path('add_pharmacy/manual/', views.add_pharmacy_m, name='add_pharmacy_m'),
    path('add_pharmacy/auto/', views.add_pharmacy_a, name='add_pharmacy_a'),
    path("pharmacy/delete/<int:id>/", views.delete_pharmacy),
    
    
    
    
    
]