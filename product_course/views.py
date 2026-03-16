from rest_framework import viewsets
from .models import ProductCourse
from .serializers import ProductCourseSerializer

class ProductCourseViewSet(viewsets.ModelViewSet):
    queryset = ProductCourse.objects.all()
    serializer_class = ProductCourseSerializer