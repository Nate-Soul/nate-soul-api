from django.urls import path
from .views import ArticleListAPIView, ArticleDetailAPIView

app_name="blogapi"
urlpatterns = [
    path("", ArticleListAPIView.as_view(), name="blog-list"),
    path("<slug:slug>/", ArticleDetailAPIView.as_view(), name="blog-detail"),
]