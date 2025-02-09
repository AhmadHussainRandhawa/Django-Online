from django.db import models
from django.utils import timezone

class Service(models.Model):
    service_types_choice = (('game_development', 'Game Development'),
    ('web_development', 'Web Development'),('data_visualizaion', 'Data Visualization'),('other', 'Other'))
    service_types = models.CharField(max_length=20, choices=service_types_choice)

    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='services/images/')
    description = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.title