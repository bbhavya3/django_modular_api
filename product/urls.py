from django.urls import path
from .views import ProductListCreate, ProductDetail

urlpatterns = [
    path('', ProductListCreate.as_view()),
    path('<int:id>/', ProductDetail.as_view()),
]