from django.urls import path
from auth_users.views import UserRegisterView, UserLoginView, UserProfileView

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='accounts_signup'),
    path('login/', UserLoginView.as_view(), name='accounts_login'),
    path('profile/', UserProfileView.as_view(), name='accounts_profile'),
]

