from rest_framework.routers import DefaultRouter
from .views import VendorProductViewSet

router = DefaultRouter()
router.register('', VendorProductViewSet)

urlpatterns = router.urls