from rest_framework.routers import DefaultRouter
from .views import ProductCourseViewSet

router = DefaultRouter()
router.register('', ProductCourseViewSet)

urlpatterns = router.urls