from django.shortcuts import render

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')
