from django.urls import path
from .views import show_map
from . import views

urlpatterns = [
    path('map/', show_map, name='show_map'),
     path('manage-requests/', views.manage_requests, name='manage_requests'),
    path('update-request-status/<int:request_id>/<str:action>/', views.update_request_status, name='update_request_status'),
    path('request-ambulance/', views.request_ambulance, name='request_ambulance'),
]
