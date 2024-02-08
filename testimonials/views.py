from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import TestimonialSerializer
from .models import Testimonial

# Create your views here.
class TestimonialListAPIView(APIView):
    
    serializer_class = TestimonialSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        processes       = Testimonial.objects.filter(is_active=True)
        serializer      = self.serializer_class(processes, many=True, context = {"request": request})
        response_data   = {
            "data": serializer.data,
            "message": "Testimonial list fetched successfully"
        }
        return Response(response_data, status=status.HTTP_200_OK)