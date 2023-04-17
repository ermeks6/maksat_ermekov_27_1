from django.http import HttpResponse
from datetime import datetime

# Create your views here.

""" MVC - Model View Controller """


def hello(request):
    return HttpResponse("Hello! It's my project")


def now_date(request):
    current_date = datetime.now().strftime("%Y-%m-%d") # Get the current date
    return HttpResponse(current_date)


def goodby(request):
    return HttpResponse("Goodbye user!")




