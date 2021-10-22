from django.conf.urls.static import static
from django.urls import include,path
from django.contrib import admin
from django.conf import settings


urlspatterns = [
    path('admin/',admin.site.urls),
    path('ckeditor/',include("ckeditor_uploaders.urls")),
    path('',include("core.urls","core"),namespace = "content"),
    path('accounts/',include("django.contrib.auth.urls")),
    
]


if settings.DEBUG:
    urlspatterns = urlspatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlspatterns = urlspatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)