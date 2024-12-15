from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    confirm_pin = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['phone', 'pin', 'confirm_pin']

    def validate(self, attrs):
        if attrs['pin'] != attrs['confirm_pin']:
            raise serializers.ValidationError({'pin': 'PINs do not match!'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_pin')
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    pin = serializers.CharField(write_only=True)

class PinResetSerializer(serializers.Serializer):
    phone = serializers.CharField()
    new_pin = serializers.CharField(write_only=True)
    confirm_new_pin = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['new_pin'] != attrs['confirm_new_pin']:
            raise serializers.ValidationError({'pin': 'New PINs do not match!'})
        return attrs
