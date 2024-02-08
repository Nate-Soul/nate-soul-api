from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    
    avatar_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Testimonial
        fields = "__all__"
    
    def get_avatar_url(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        return None
