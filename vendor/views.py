from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Vendor
from .serializers import VendorSerializer


class VendorListCreate(APIView):

    def get(self, request):

        vendors = Vendor.objects.filter(is_active=True)

        serializer = VendorSerializer(vendors, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = VendorSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorDetail(APIView):

    def get_object(self, id):

        try:
            return Vendor.objects.get(id=id)

        except Vendor.DoesNotExist:
            return None


    def get(self, request, id):

        vendor = self.get_object(id)

        if not vendor:
            return Response({"error": "Vendor not found"}, status=404)

        serializer = VendorSerializer(vendor)

        return Response(serializer.data)


    def put(self, request, id):

        vendor = self.get_object(id)

        serializer = VendorSerializer(vendor, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


    def patch(self, request, id):

        vendor = self.get_object(id)

        serializer = VendorSerializer(vendor, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request, id):

        vendor = self.get_object(id)

        vendor.delete()

        return Response(status=204)