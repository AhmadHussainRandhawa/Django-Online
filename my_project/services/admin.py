from django.contrib import admin
from .models import Service, ServiceReview, WebStore, ServiceCertificate

class ServiceReviewInline(admin.TabularInline): # TabularInline: allows you to embed related models (child models) directly into the admin interface of a parent model.
    model = ServiceReview
    extra = 2

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_types', 'date')
    inlines = [ServiceReviewInline]

class WebStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('store_service_link', )

class ServiceCertificateAdmin(admin.ModelAdmin):
    list_display = ('service_certificate_link', 'certificate_number')


# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(WebStore, WebStoreAdmin)
admin.site.register(ServiceCertificate, ServiceCertificateAdmin)