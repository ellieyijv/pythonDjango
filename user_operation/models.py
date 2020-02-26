from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

# Create your models here.
User = get_user_model()

class UserFav(models.Model):
    """
    User Favourite
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="Goods", help_text="Goods Id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = 'User Favourite'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username


class UserLeavingMessage(models.Model):
    """
    User Message
    """
    MESSAGE_CHOICES = (
        (1, "Notes"),
        (2, "Complain"),
        (3, "Enquire"),
        (4, "Support"),
        (5, "Buy")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="Message Type",
                                      help_text="Types: 1(Notes),2(Complain),3(Enquire),4(Support),5(Buy)")
    subject = models.CharField(max_length=100, default="", verbose_name="Subject")
    message = models.TextField(default="", verbose_name="Message Content", help_text="Message Content")
    file = models.FileField(upload_to="message/images/", verbose_name="Upload File", help_text="Upload File")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "User Leaving Message"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    """
    User Shipping Address
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User" )
    province = models.CharField(max_length=100, default="", verbose_name="Province")
    city = models.CharField(max_length=100, default="", verbose_name="City")
    district = models.CharField(max_length=100, default="", verbose_name="Ditrict")
    address = models.CharField(max_length=100, default="", verbose_name="Address")
    signer_name = models.CharField(max_length=100, default="", verbose_name="Signer")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="Mobile")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
