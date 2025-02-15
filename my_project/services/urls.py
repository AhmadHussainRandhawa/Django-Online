from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_services, name='all_services'),
    path('<int:service_id>/', views.service_detail, name='service_detail'),
    path('service_stores/', views.service_store_view, name='service_store')
]
