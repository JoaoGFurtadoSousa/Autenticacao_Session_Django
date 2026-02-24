
from django.contrib import admin
from django.urls import path, include
from users.views import login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_user),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('cars.urls'),)
]
