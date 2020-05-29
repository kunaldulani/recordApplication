from django.shortcuts import render
from django.http import HttpResponse
from .models import Application

# My vies/routes

# Home Page
def index(request):
    return render(request, "recordApp/index.html")

# Display all applications
def allApplications(request):
    context = {
        "applications": Application.objects.all()
    }
    return render(request, "recordApp/allApplications.html", context)
