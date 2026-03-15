from django.urls import path
from .views import CertificationListCreate

urlpatterns = [

    path('certifications/', CertificationListCreate.as_view()),

]