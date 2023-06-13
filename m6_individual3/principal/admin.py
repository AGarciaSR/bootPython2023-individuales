from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from principal.models import AppUser

class AppUserInline(admin.StackedInline):
    model = AppUser
    can_delete = False
    verbose_name_plural = "appuser"
    

# Register your models here.
