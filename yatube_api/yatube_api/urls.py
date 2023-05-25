from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
]
