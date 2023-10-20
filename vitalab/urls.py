from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('exames/', include('exames.urls')),
    path('empresarial/', include('empresarial.urls')),
    path('', lambda request: redirect('/usuarios/login')),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
