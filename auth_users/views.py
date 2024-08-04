from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.utils.translation import gettext as _

from auth_users.serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from auth_users.token.jwt import  get_tokens_for_user

# Create your views here.


class UserRegisterView(generics.GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = get_tokens_for_user(user=user)
        data = {
            'message': _('You are successfully Register'),
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'tokens': tokens
        }
        return Response(data=data, status=200, )

class UserLoginView(generics.GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        tokens = get_tokens_for_user(user=user)
        data = {
            'message': _('You are successfully Login'),
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'tokens': tokens
        }
        return Response(data=data, status=200, )
    
class UserProfileView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
