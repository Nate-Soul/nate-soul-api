from django.urls import path
from .views import (
    ProjectListAPIView,
    ProjectDetailAPIView,
    RelatedProjectsView
)

app_name = "projects"
urlpatterns = [
    path('', ProjectListAPIView.as_view(), name="project-list"),
    path('<slug:slug>/', ProjectDetailAPIView.as_view(), name="project-detail"),
    path('<slug:slug>/related/', RelatedProjectsView.as_view(), name="related-projects"),
]