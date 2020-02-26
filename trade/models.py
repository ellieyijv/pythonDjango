from datetime import datetime 
from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods
User = get_user_model()
# Create your models here.

class ShoppingCart(models.Model):
    """
    shopping cart
    """
    user =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    goods =  models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="Goods")
    nums = models.IntegerField(default=0, verbose_name="Quantity")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "Shopping Cart"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")
    
    def __str__(self):
        return "%s %d".format(self.goods.name, self.nums)

class OrderInfo(models.Model):
    """
    Order Info
    """

    ORDER_STATUS = (
        ("TRADE_SUCCESS", "Success"),
        ("TRADE_CLOSED", "Closed"),
        ("WAIT_BUYER_PAY", "Start_Trade"),
        ("TRADE_FINISHED", "Close_Trade"),
        ("PAYING", "Paying"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="Order Serial Number")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"Trade Number")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="Order Status")
    post_script = models.CharField(max_length=200, verbose_name="Notes")
    order_mount = models.FloatField(default=0.0, verbose_name="Order Amount")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="Paying Time")

    # 用户信息
    address = models.CharField(max_length=100, default="", verbose_name="Shipping Address")
    signer_name = models.CharField(max_length=20, default="", verbose_name="Signer")
    singer_mobile = models.CharField(max_length=11, verbose_name="Signer Mobile")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    Order Details
    """
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="Order Info", related_name="goods")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="Goods")
    goods_num = models.IntegerField(default=0, verbose_name="Quantity of Goods")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "Order Details"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)