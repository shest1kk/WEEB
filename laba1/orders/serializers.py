from rest_framework import serializers
from .models import Car


class CarSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = ['category', 'brand', 'model', 'description', 'license_plate', 'available']
