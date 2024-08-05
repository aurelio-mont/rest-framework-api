from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView
from auth_users.views import UserRegisterView, UserLoginView, UserProfileView, UserLogoutView

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='accounts_signup'),
    path('login/', UserLoginView.as_view(), name='accounts_login'),
    path('profile/', UserProfileView.as_view(), name='accounts_profile'),
    path('logout/', UserLogoutView.as_view(), name='accounts_logout'),
]

