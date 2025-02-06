from django.http import HttpResponse  
from django.shortcuts import render


def home(request):
    return render(request, 'website/index.html') # it will look for index.html in templates folder

def contact(request):
    return HttpResponse("Hello, This is contact page")  # it will return this string

def about(request):
    return HttpResponse("Hello, This is about page")

