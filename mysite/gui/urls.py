from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # ex: /gui/
    path('', views.index, name='index'),
    # ex: /gui/about
    path('about', views.about, name='about'),
    # ex: /gui/contact
    path('contact', views.contact, name='contact'),
    # ex: /gui/portfolio
    path('portfolio', views.portfolio, name='portfolio'),
    # ex: /gui/portfolio-single
    path('portfolio-single', views.portfolio_single, name='portfolio-single'),
    # ex: /gui/portfolio-single/1
    path('portfolio-single/<int:project_id>', views.portfolio_single_s, name='portfolio-single-s'),
    # ex: /gui/services
    path('services', views.services, name='services'),
]
