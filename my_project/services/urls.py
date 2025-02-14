from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_services, name='all_services'),
    path('special_services/', views.special_services, name='special_services'),
    path('<int:service_id>/', views.service_detail, name='service_detail'),
]
