from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import requests

# Page Requests
def index(request):
    return render(request,"gui/index.html")

def about(request):
    return render(request,"gui/about.html")

def contact(request):
    return render(request,"gui/contact.html")

def portfolio(request):
    return render(request,"gui/portfolio.html")

def portfolio_single(request):
    return render(request,"gui/portfolio-single.html")

def services(request):
    return render(request,"gui/services.html")

