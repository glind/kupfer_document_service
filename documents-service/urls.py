from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


# openapi implementation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_info = openapi.Info(
        title="Documents Service API",
        default_version='latest',
        description="A microservice which handles file up- and downloads to an Amazon S3 Bucket.",
)

schema_view = get_schema_view(
    swagger_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^docs/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('health_check/', include('health_check.urls')),
    path('', include('api.urls')),
]

urlpatterns += staticfiles_urlpatterns() \
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
