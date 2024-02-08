from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    
    icon_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Service
        fields = "__all__"
    
    def get_icon_url(self, obj):
        if obj.icon:
            return self.context['request'].build_absolute_uri(obj.icon.url)
        return None
