from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # ex: /api/send-contact
    path('send-contact', views.send_contact, name='send-contact'),
]
