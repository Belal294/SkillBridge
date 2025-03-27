from rest_framework import serializers
from .models import Order
from services.models import Service

class OrderSerializer(serializers.ModelSerializer):
   
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'buyer', 'service', 'status', 'created_at', 'updated_at', 'order_date']

    def create(self, validated_data):
        
        validated_data['buyer'] = self.context['request'].user
        return super().create(validated_data)
