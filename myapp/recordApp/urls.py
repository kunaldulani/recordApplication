from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("allApplications", views.allApplications)
]
