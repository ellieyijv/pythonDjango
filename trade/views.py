from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly
from .serializers import ShoppingCartSerializer,OrderDetailsSerializer, ShoppingCartDetailSerializer, OrderSerializer
from .models import ShoppingCart, OrderInfo, OrderGoods

# Create your views here.
class ShoppingCartViewset(viewsets.ModelViewSet):
    serializer_class = ShoppingCartSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
  
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field="goods_id"

    def get_serializer_class(self):
        if self.action == "list":
            return ShoppingCartDetailSerializer
        else:
            return ShoppingCartSerializer
    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        shopping_cart = serializer.save()
        goods = shopping_cart.goods
        goods.goods_num -= shopping_cart.nums
        goods.save()
    
    def perform_destroy(self, instance):
        goods = instance.goods
        goods.goods_num += instance.nums
        goods.save()    
        instance.delete()

    def perform_update(self, serializer):
        existed_record = ShoppingCart.objects.get(id=serializer.instance.id)
        existed_nums = existed_record.nums
        saved_record = serializer.save()
        nums = saved_record.nums - existed_nums
        goods = saved_record.goods
        goods.goods_num -= nums
        goods.save()    

class OrderViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
  
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailsSerializer
        return OrderSerializer

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)
     
    def perform_create(self, serializer):
        order = serializer.save()
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.goods_num = shop_cart.nums
            order_goods.order = order
            order_goods.save()
            shop_cart.delete()
        return order