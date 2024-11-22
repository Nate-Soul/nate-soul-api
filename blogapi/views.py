from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

# Create your views here.
class CustomPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 20

class ArticleListAPIView(APIView):
    
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        paginator  = CustomPagination()
        queryset   = Article.objects.filter(status="published")
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)

class ArticleDetailAPIView(APIView):

    model_class         = Article
    serializer_class    = ArticleSerializer
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get_object(self, slug):
        return get_object_or_404(self.model_class, slug=slug)
    
    def get(self, request, slug, *args, **kwargs):
        project = self.get_object(slug)
        serializer = self.serializer_class(project, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

