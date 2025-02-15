from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Service(models.Model):
    service_types_choice = (('game_development', 'Game Development'),
    ('web_development', 'Web Development'),('data_visualizaion', 'Data Visualization'),('other', 'Other'))
    service_types = models.CharField(max_length=20, choices=service_types_choice)

    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='services/images/')
    description = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# One to many relationship between Service and ServiceReviews
class ServiceReview(models.Model):
    review_service_link = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.name} review for {self.service.title}"

# Many to Many Relationship
class WebStore(models.Model):
    store_service_link = models.ManyToManyField(Service, on_delete=models.CASCADE, related_name='store')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# one to one relationship
class ServiceCertificate(models.Model):
    service_certificate_link = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField()
    issued_date = models.DateTimeField()
    due_date = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.service_certificate_link.title}"
