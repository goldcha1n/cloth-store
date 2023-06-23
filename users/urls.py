from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (UserEmailVerificationView, UserLoginView, UserProfileView,
                    UserRegistrationView)

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', UserEmailVerificationView.as_view(), name='email_verification'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
]
