from django.urls import path
from .views import ServiceListAPIView

app_name = "services"
urlpatterns = [
    path('', ServiceListAPIView.as_view(), name="service-list"),
]
