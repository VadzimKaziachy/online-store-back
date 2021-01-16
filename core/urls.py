from django.contrib import admin
from django.urls import path, include

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
