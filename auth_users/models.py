from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
import uuid

from auth_users.managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    sur_name = models.CharField(_('sur_name'), blank=True, max_length=150)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.email