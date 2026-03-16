from rest_framework import serializers
from .models import CourseCertification

class CourseCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertification
        fields = '__all__'