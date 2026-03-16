from rest_framework import serializers
from .models import VendorProduct

class VendorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProduct
        fields = '__all__'