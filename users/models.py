
from  datetime import datetime
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """
    user
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="User Name")
    birthday = models.DateField(null=True, blank=True, verbose_name="Birthday")
    mobile = models.CharField(max_length=11, verbose_name="Mobile")
    gender = models.CharField(max_length=6, choices=(('male','male'),('female','female')), default="male", verbose_name="Gender")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="Email")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    verify code
    """

    code = models.CharField(max_length=10, verbose_name="Verify Code")
    mobile = models.CharField(max_length=11, verbose_name="Phone")
    add_time = models.DateTimeField(default = datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "Verify Code"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code