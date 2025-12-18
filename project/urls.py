from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path




urlpatterns = [
    path('admin_bo`lib_kirish/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('app.urls')),
    path('', include('accounts.urls')),

]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


