from django.urls import path, include
from auth_users.views import UserRegisterView

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='accounts_signup')
]

