from rest_framework import serializers
from .models import Service, Category, ServiceImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ServiceImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ServiceImage
        fields = ['id', 'image']

# class ServiceSerializer(serializers.ModelSerializer):
#     images = ServiceImageSerializer(many=True, read_only=True)

#     class Meta:
#         model = Service
#         fields = ['id', 'title', 'description', 'price', 'category', 'delivery_time', 'created_at', 'images']
#         # fields = '__all__'



class ServiceSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(many=True, read_only=True, source='serviceimage_set')

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'price', 'category', 'delivery_time', 'created_at', 'images']
