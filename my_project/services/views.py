from django.shortcuts import render, get_object_or_404
from .models import Service

def all_services(request):
    services = Service.objects.all()        # get all rows from Service's model table in database.
    return render(request, 'services/all_services.html', {'services': services}) # 'service' for template to use it.
    # it look for all_services.html in templates folder cuz templates are defined in settings.py

def special_services(request):
    return render(request, 'services/special_services.html')

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'services/service_detail.html', {'service': service})
