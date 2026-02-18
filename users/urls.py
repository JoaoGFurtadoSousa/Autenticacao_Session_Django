from django.urls import path
from .views import register_user, login_user, logout, home

urlpatterns = [
   path('registerUser', register_user, name= 'register_user'),
   path('login', login_user, name = "login_user"),
   path('logout', logout, name = 'logout_user'),
   path('home', home, name = 'home')
]