from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ProcessSerializer
from .models import Process

# Create your views here.
class ProcessListAPIView(APIView):
    
    serializer_class = ProcessSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        processes = Process.objects.all()
        serializer = self.serializer_class(processes, many=True, context={"request": request})
        response = {
            "data": serializer.data,
            "message": "Process list fetched successfully"
        }
        return Response(response, status=status.HTTP_200_OK)