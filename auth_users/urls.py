from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from auth_users.views import  UserAllView, UserRegisterView, UserLoginView, UserProfileView, UserLogoutView

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='accounts_signup'),
    path('login/', UserLoginView.as_view(), name='accounts_login'),
    path('logout/', UserLogoutView.as_view(), name='accounts_logout'),
    path('profile/', UserProfileView.as_view(), name='accounts_profile'),
    path('logout/', UserLogoutView.as_view(), name='accounts_logout'),
    path('users/', UserAllView.as_view(), name='accounts_users'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

