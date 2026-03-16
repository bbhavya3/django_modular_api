from rest_framework import serializers
from .models import ProductCourse

class ProductCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCourse
        fields = '__all__'