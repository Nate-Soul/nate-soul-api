from django.urls import path
from .views import AccountDetailAPIView

app_name = "accounts"
urlpatterns = [
    path('<str:username>/', AccountDetailAPIView.as_view(), name="account-detail"),
]
