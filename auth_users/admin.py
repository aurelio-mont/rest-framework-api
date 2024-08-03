from django.contrib import admin

import auth_users

# Register your models here.
admin.site.register(
    auth_users.models.CustomUser
)

