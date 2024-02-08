from django.urls import path
from .views import TestimonialListAPIView

app_name = "testimonials"
urlpatterns = [
    path('', TestimonialListAPIView.as_view(), name="testimonial-list"),
]
