from django.utils.text import slugify
from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": [slugify("name"),]
    }
admin.site.register(Service, ServiceAdmin)