from django.http import HttpResponse  
from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html') # it will look for home.html in templates folder

def about(request):
    return HttpResponse("This is the about page")

