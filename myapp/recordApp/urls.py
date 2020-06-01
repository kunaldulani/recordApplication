from django.urls import path
from .addToCalendar import startup

from . import views

urlpatterns = [
    path("", views.index),
    path("allApplications", views.allApplications)
]

startup()
