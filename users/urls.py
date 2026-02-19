from django.urls import path
from .views import register_user, login_user, logout_user, home, change_user, exclude_user, create_user

urlpatterns = [
   path('registerUser', register_user, name= 'register_user'),
   path('login', login_user, name = "login_user"),
   path('logout', logout_user, name = 'logout_user'),
   path('home', home, name = 'home'),
   path('change_user/<int:pk>', change_user, name = 'change_user'),
   path('exclude_user/<int:pk>', exclude_user, name = 'exclude_user'),
   path('create_user', create_user, name = 'create_user')
]