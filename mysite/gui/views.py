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

def portfolio_single_s(request, project_id): 
    context = [{
               'project_title':'DLandry Beach Houses',
               'project_details_1':"This project is hopefully one of our many projects in the vacation rental industry. We've built a website for our client that accuratly describes their rental business in a nicely styled design.",
               'project_details_2':"It integrates with their VRBO page with booking, and has it's own payment processing system to help the client bypass all charges that rental sites like VRBO normally require.",
               'roles':'HTML, CSS, Javascript/Jquery, Python/Flask/Django, MySQL, Microservice, AWS EC2',
               'client':'DLandry Beach Houses',
               'website_link':"http://dlandrybeachhouses.com:5000",
               'pic_1':'project_1.PNG'
    },{
               'project_title':'Bluemarble',
               'project_details_1':"This project is one of a few projects dealt with one of our most loyal clients. It helps with the process of easily designing skills for Amazon Alexa by having to code as little as possible to create interesting Alexa apps.",
               'project_details_2':"We're proud to say that our team completed the majority of the application which is still being used today.",
               'roles':'HTML, CSS, Javascript/Jquery, Python/Flask, Microservice, AWS EC2/Lambda, Amazon Alexa, Web Scraping/Automation',
               'client':'Bluemarble',
               'website_link':"",
               'pic_1':'project_2.jpg'
    },{
               'project_title':'Appto Health',
               'project_details_1':"This project is for the healthcare field that helps with communication between hospital employees to help them become more efficient and productive.",
               'project_details_2':"Our team helped create some of the graphical features for this site including input wizards, modals, and administration pages.",
               'roles':'HTML, CSS, Javascript/Jquery, PHP/MySQL',
               'client':'Appto Health',
               'website_link':"https://www.apptohealth.com",
               'pic_1':'project_3.PNG'
    },{
               'project_title':'Tablelead',
               'project_details_1':"This project aims to use pre-existing data from many local resturants in order to help the client (a potential resturant business) learn more about what type of business they should build to become more locally competitive.",
               'project_details_2':"Our team helped with the gathering process of collecting Big Data in order to support the AI systems of the application.",
               'roles':'Python/Flask, MySQL, Microservice, Web Scraping/Automation',
               'client':'Tablelead',
               'website_link':"https://www.tablelead.com",
               'pic_1':'project_4.PNG'
    }]



    return render(request,"gui/portfolio-single.html", context[project_id-1])

def services(request):
    return render(request,"gui/services.html")

