from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    #path('request-ambulance/<str:hospital_id>/', views.request_ambulance, name='request_ambulance'),


]
