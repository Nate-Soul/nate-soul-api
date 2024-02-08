from django.contrib import admin
from django.utils.text import slugify
from .models import Process

# Register your models here.
class ProcessAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (slugify('name'),),
    }
admin.site.register(Process, ProcessAdmin)