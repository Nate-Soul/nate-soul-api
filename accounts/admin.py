from django.contrib import admin

from .models import Social, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Social)