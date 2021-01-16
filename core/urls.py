from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(
        [
            path('schema/', include(
                [
                    path('', SpectacularAPIView.as_view(), name='schema'),
                    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
                    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                ]
            )),
            path('products/', include('products.urls')),
            path('categories/', include('categories.urls')),
        ]
    )),
]


if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)