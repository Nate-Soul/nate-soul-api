from django.urls import path
from .views import ProcessListAPIView

app_name = "processes"
urlpatterns = [
    path('', ProcessListAPIView.as_view(), name="process-list"),
]
