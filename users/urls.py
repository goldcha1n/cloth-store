from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
]