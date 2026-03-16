from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Certification
from .serializers import CertificationSerializer


class CertificationListCreate(APIView):

    def get(self, request):
        certs = Certification.objects.all()
        serializer = CertificationSerializer(certs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CertificationDetail(APIView):

    def get_object(self, id):
        try:
            return Certification.objects.get(id=id)
        except Certification.DoesNotExist:
            return None

    def get(self, request, id):
        cert = self.get_object(id)
        if not cert:
            return Response({"error": "Certification not found"}, status=404)
        serializer = CertificationSerializer(cert)
        return Response(serializer.data)

    def put(self, request, id):
        cert = self.get_object(id)
        if not cert:
            return Response({"error": "Certification not found"}, status=404)

        serializer = CertificationSerializer(cert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, id):
        cert = self.get_object(id)
        if not cert:
            return Response({"error": "Certification not found"}, status=404)

        cert.delete()
        return Response(status=204)