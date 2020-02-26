from .models import UserFav, UserLeavingMessage, UserAddress
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator 
from goods.serializers import GoodsSerializer

class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    class Meta:
        model = UserFav
        validators=[
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=("user", "goods"),
                message="already Favourated"
            )
        ]
        fields = ("user", "goods", "id")


class UserFavDetailsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()
    class Meta:
        model = UserFav
        fields = ("goods", "id")


class UserLeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ("message", "user", "subject","file","message_type", "id", "add_time")

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    
    signer_name=serializers.CharField(required=True, error_messages={
        "blank": "please type in the name",
        "required": "Please type in the name"
    })

    class Meta:
        model = UserAddress
        fields = ("user", "province", "city", "district","address", "signer_name", "signer_mobile","add_time", "id")