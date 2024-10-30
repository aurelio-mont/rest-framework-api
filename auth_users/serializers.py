from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _

from auth_users.models import CustomUser as User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        
        model = User
        fields = ['id', 'email', 'full_name', 'date_of_birth']

    def get_full_name(self, obj):
        return '{} {} {}'.format(obj.first_name, obj.last_name, obj.sur_name) 

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password']
    
    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(_('Unable to log in with provided credentials'))
