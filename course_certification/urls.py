from rest_framework.routers import DefaultRouter
from .views import CourseCertificationViewSet

router = DefaultRouter()
router.register('', CourseCertificationViewSet)

urlpatterns = router.urls