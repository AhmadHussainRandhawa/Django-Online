from django.shortcuts import render, get_object_or_404
from .models import Service, WebStore
from .forms import ServiceForm

def all_services(request):
    services = Service.objects.all()        # get all rows from Service's model table in database.
    return render(request, 'services/all_services.html', {'services': services}) # 'service' for template to use it.
    # it look for all_services.html in templates folder cuz templates are defined in settings.py

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'services/service_detail.html', {'service': service})

def service_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
           service_type = form.cleaned_data['service']
           stores = WebStore.objects.filter(store_service_link=service_type)
    else:
        form = ServiceForm()  # Initialize the form

    return render(request, 'services/service_stores.html', {'stores': stores, 'form' : form}) 