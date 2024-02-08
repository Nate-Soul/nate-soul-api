from django.urls import path
from .views import (
    ProjectListAPIView,
    ProjectDetailAPIView
)

app_name = "projects"
urlpatterns = [
    path('', ProjectListAPIView.as_view(), name="project-list"),
    path('<slug:slug>/', ProjectDetailAPIView.as_view(), name="project-detail"),
]