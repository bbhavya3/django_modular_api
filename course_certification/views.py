from rest_framework import viewsets
from .models import CourseCertification
from .serializers import CourseCertificationSerializer

class CourseCertificationViewSet(viewsets.ModelViewSet):
    queryset = CourseCertification.objects.all()
    serializer_class = CourseCertificationSerializer
