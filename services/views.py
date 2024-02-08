from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ServiceSerializer
from .models import Service

# Create your views here.
class ServiceListAPIView(APIView):
    
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        processes   = Service.objects.filter(is_active=True)
        serializer  = self.serializer_class(processes, many=True, context = {"request": request})
        response    = {
            "data": serializer.data,
            "message": "Service list fetched successfully"
        }
        return Response(response, status=status.HTTP_200_OK)