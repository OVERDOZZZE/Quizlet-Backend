from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Card.views import start


urlpatterns = [
    path('admin/', admin.site.urls),
    path('modules/', include('Card.urls')),
    path('user/', include('User.urls')),
    path('', start)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
