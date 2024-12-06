from django.shortcuts import render,redirect

def show_map(request):
    return render(request, 'map.html')
from django.shortcuts import render
from .models import AmbulanceRequest

def manage_requests(request):
    requests = AmbulanceRequest.objects.filter(status='Pending')
    return render(request, 'hospital/manage_requests.html', {'requests': requests})

def update_request_status(request, request_id, action):
    ambulance_request = AmbulanceRequest.objects.get(id=request_id)
    if action == 'accept':
        ambulance_request.status = 'Accepted'
    elif action == 'decline':
        ambulance_request.status = 'Declined'
    ambulance_request.save()
    return redirect('manage_requests')
from django.shortcuts import render

def request_ambulance(request):
    # Your logic for handling the ambulance request
    return render(request, 'request_ambulance.html')
