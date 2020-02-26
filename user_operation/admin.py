from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import UserFav

# Register your models here.
class UserFavAdmin(admin.ModelAdmin):
    fields = ("user", "goods", "add_time")
admin.site.register(UserFav, UserFavAdmin)