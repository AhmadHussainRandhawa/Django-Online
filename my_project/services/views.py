from django.shortcuts import render

def services(request):
    # it look for all_services.html in templates folder cuz templates are defined in settings.py
    return render(request, 'services/all_services.html')

def specialServices(request):
    return render(request, 'services/specialServices.html')
