from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile, Social
    
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"
        

class ProfileSerializer(serializers.ModelSerializer):
    social          = SocialSerializer(many=True, read_only=True)
    headshot_url    = serializers.SerializerMethodField()
    profile_img_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_headshot_url(self, obj):
        if obj.headshot:
            return self.context['request'].build_absolute_uri(obj.headshot.url)
        return None

    def get_profile_img_url(self, obj):
        if obj.profile_img:
            return self.context['request'].build_absolute_uri(obj.profile_img.url)
        return None
    

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    
    class Meta:    
        model   = User
        fields  = ("username", "email", "first_name", "last_name", "profile")
