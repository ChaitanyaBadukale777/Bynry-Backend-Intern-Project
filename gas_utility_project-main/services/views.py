# services/views.py
from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def create_request(request):
    if request.method == 'POST':  # If form is submitted via POST request
        form = ServiceRequestForm(request.POST, request.FILES)  # Pass form data
        if form.is_valid():  # If the form is valid
            form.save()  # Save the form data to the database
            return redirect('track_request')  # Redirect to request tracking page
    else:
        form = ServiceRequestForm()  # Create a blank form if it's a GET request
    return render(request, 'services/create_request.html', {'form': form})

def track_request(request):
    service_requests = ServiceRequest.objects.all()  # Get all requests from the database
    return render(request, 'services/track_request.html', {'service_requests': service_requests})
