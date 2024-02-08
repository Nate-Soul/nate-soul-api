from rest_framework import serializers
from .models import (
    Project, 
    ProjectImage,
    Category,
    Tag,
    Feature,
    Technology
)
from services.serializers import ServiceSerializer

class ProjectImageSerializer(serializers.ModelSerializer):
    
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ProjectImage
        fields = "__all__"
        
        
    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = "__all__"
        
class TechnologySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Technology
        fields = "__all__"
        
class FeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feature
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    
    tags            = TagSerializer(many=True, read_only=True)
    categories      = CategorySerializer(many=True, read_only=True)
    technologies    = TechnologySerializer(many=True, read_only=True)
    services        = ServiceSerializer(many=True, read_only=True)
    features        = FeatureSerializer(many=True, read_only=True)
    images          = ProjectImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = "__all__"