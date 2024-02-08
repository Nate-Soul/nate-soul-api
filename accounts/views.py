from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from .serializers import (
    # ProfileSerializer, 
    UserSerializer
)
# from .models import Profile

# Create your views here.
class AccountDetailAPIView(APIView):
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get_object(self, username):
        return get_object_or_404(User, username=username)
        
    def get(self, request, username, *args, **kwargs):
        account = self.get_object(username)
        serializer = UserSerializer(account, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)