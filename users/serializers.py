import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from rest_framework.validators import UniqueValidator

from .models import VerifyCode

from MxShop.settings import REGEX_MOBILE

User = get_user_model()

class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        # check the mobile, using filter than the get
        if User.objects.filter(mobile = mobile).count():
            raise serializers.ValidationError("User already exsit")
        #check the mobile 
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("Mobile is not correct")

        #verify the frequence of the sending
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError("less than 60 seconds since last sending")

        return mobile


class UserDetailSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile")


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="Verify Code",
                                error_messages={
                                    "blank": "Please type in verify code",
                                    "required": "Please type in verify code",
                                    "max_length": "Verify code is wrong",
                                    "min_length": "Verify code is wrong"
                                },
                                help_text="Verify Code")
    username = serializers.CharField(label="User Name", help_text="User Name", required=True, allow_blank=False,
                                    validators=[UniqueValidator(queryset=User.objects.all(), message="User is already exsit")])

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="Password", label="Password", write_only=True,
    )

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]

            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_mintes_ago > last_record.add_time:
                raise serializers.ValidationError("Code is expired")

            if last_record.code != code:
                raise serializers.ValidationError("Verify code is wrong")

        else:
            raise serializers.ValidationError("Verify code is wrong")

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile", "password")