from django.contrib import admin

# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserProfile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserProfile
    list_display = ['name', 'birthday', 'mobile', 'gender', 'email']

admin.site.register(UserProfile, CustomUserAdmin)