from django.urls import path
from .views import CertificationListCreate, CertificationDetail

urlpatterns = [
    path('', CertificationListCreate.as_view()),
    path('<int:id>/', CertificationDetail.as_view()),
]