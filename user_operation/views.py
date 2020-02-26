from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .models import UserFav, UserLeavingMessage, UserAddress
from utils.permissions import IsOwnerOrReadOnly
from .serializers import UserFavSerializer, UserFavDetailsSerializer, UserLeavingMessageSerializer, AddressSerializer
# Create your views here.

class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
  
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user = self.request.user)
    #same function, can write in the signals
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     goods = instance.goods
    #     goods.fav_num += 1
    #     goods.save()

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailsSerializer
        elif self.action == "create":
            return UserFavSerializer
        return UserFavSerializer


class LeavingMessageViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = UserLeavingMessageSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
  
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)

#if inherit all the create, list, update, destroy, and generic, then using modelviewset instead

class AddressViewset(viewsets.ModelViewSet):

    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
