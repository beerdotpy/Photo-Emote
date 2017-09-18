from rest_framework import serializers
from models import Image,User

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image_id', 'url', 'user', 'created_at', 'description', 'hashtags', 'orientation')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
	model = User
	fields = ('device_id', 'user_id')
