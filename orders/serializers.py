from . models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # extra_kwargs = {'size': {'required': True}}
        fields = '__all__'