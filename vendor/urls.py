from django.urls import path
from .views import VendorListCreate, VendorDetail

urlpatterns = [
    path('', VendorListCreate.as_view()),
    path('<int:id>/', VendorDetail.as_view()),
]