from django.shortcuts import render
from django.http import HttpResponse

# My vies/routes

def index(request):
    return HttpResponse("Hello World")
