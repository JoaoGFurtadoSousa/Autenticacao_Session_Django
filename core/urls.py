
from django.contrib import admin
from django.urls import path, include
from users.views import login_user
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_user),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('cars.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
