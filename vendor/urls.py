from django.urls import path
from .views import VendorListCreate, VendorDetail

urlpatterns = [
    # GET -> list vendors
    # POST -> create vendor
    path('', VendorListCreate.as_view(), name='vendor-list-create'),

    # GET -> vendor details
    # PUT/PATCH -> update vendor
    # DELETE -> delete vendor
    path('<int:id>/', VendorDetail.as_view(), name='vendor-detail'),
]