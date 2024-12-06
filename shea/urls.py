from django.urls import include, path

urlpatterns = [
    path('hospital/', include('hospital.urls')),
    path('patient/', include('patient.urls')), 
]
