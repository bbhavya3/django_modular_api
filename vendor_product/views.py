from rest_framework import viewsets
from .models import VendorProduct
from .serializers import VendorProductSerializer

class VendorProductViewSet(viewsets.ModelViewSet):
    queryset = VendorProduct.objects.all()
    serializer_class = VendorProductSerializer