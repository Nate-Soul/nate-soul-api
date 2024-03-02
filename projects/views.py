from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    ProjectSerializer, 
    TagSerializer, 
    CategorySerializer, 
    TechnologySerializer
)
from .models import (
    Project, 
    Tag, 
    Category,
    Technology
)

# Create your views here.
class CustomPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 20

class ProjectListAPIView(APIView):
    
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        paginator  = CustomPagination()
        queryset   = Project.objects.filter(is_active=True)
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)
    
class ProjectDetailAPIView(APIView):
    
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model_class = Project
    
    def get_object(self, slug):
        return get_object_or_404(self.model_class, slug=slug)
    
    def get(self, request, slug, *args, **kwargs):
        project = self.get_object(slug)
        serializer = self.serializer_class(project, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class RelatedProjectsView(APIView):
    
    serializer_class    = ProjectSerializer
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)
    model_class         = Project
    
    def get_object(self, slug):
        return get_object_or_404(self.model_class, slug=slug)
    
    def get(self, request, slug, *args, **kwargs):
        project = self.get_object(slug)
        related_projects = self.model_class.objects.filter(services__in=project.services.all()).exclude(id=project.id).distinct()
        serializer = self.serializer_class(related_projects, many=True, context = {"request": request})
        response_context = {
            "data": serializer.data, 
            "message": "Related projects fetched successfully"
        }
        return Response(response_context, status=status.HTTP_200_OK)
        
class TagListAPIView(APIView):
    
    model_class        = Tag 
    serializer_class   = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        tags = self.model_class.objects.all()
        serializer = self.serializer_class(tags, many=True)
        response = {
            "data": serializer.data,
            "message": "tags fetched successfully"
        }
        return Response(response, status=status.HTTP_200_OK)

class CategoryListAPIView(APIView):
    
    model_class        = Category 
    serializer_class   = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        categories = self.model_class.objects.filter(is_active=True)
        serializer = self.serializer_class(categories, many=True)
        context = {
            "data": serializer.data,
            "message": "categories fetched successfully"
        }
        return Response(context, status=status.HTTP_200_OK)
    
class TechnologyListAPIView(APIView):
    
    model_class        = Technology 
    serializer_class   = TechnologySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        technologies    = self.model_class.objects.all()
        serializer      = self.serializer_class(technologies, many=True)
        context         = {
            "data": serializer.data,
            "message": "technologies fetched successfully"
        }
        return Response(context, status=status.HTTP_200_OK)
    