from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


def home(request):
    return HttpResponse("Modular Vendor Product Course Certification API is running")


schema_view = get_schema_view(
    openapi.Info(
        title="Modular Vendor Product Course Certification API",
        default_version='v1',
        description="Backend API for managing Vendors, Products, Courses and Certifications",
        contact=openapi.Contact(email="2400032796cse4@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    path('api/vendors/', include('vendor.urls')),
    path('api/products/', include('product.urls')),
    path('api/courses/', include('course.urls')),
    path('api/certifications/', include('certification.urls')),

    path('api/vendor-products/', include('vendor_product.urls')),
    path('api/product-courses/', include('product_course.urls')),
    path('api/course-certifications/', include('course_certification.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]