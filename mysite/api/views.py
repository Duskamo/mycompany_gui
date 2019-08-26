from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests

# Data Requests
@csrf_exempt
def send_contact(request):
    if request.is_ajax() and request.method == "POST":
        # Gather Data
        contactInfo = request.body.decode('utf-8')

        # Process Data
        contactServiceUrl = "http://localhost:5001/contact"
        requests.post(contactServiceUrl,json=contactInfo)

    # return status code
    return HttpResponse("200")
