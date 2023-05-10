from django.contrib import admin
# Customize the list display of the default django user on the admin site
from django.contrib.auth.admin import UserAdmin
# Import the model
from . models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')

admin.site.register(User, CustomUserAdmin)
