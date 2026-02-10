from django.urls import path
from .views import register_user

urlpatterns = [
   path('registerUser', register_user, name= 'register_user')
]