from django.urls import path
from .views import CourseListCreate, CourseDetail

urlpatterns = [
    path('', CourseListCreate.as_view()),
    path('<int:id>/', CourseDetail.as_view()),
]