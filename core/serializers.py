from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    pin = serializers.CharField(write_only=True, min_length=4, max_length=6)
    confirm_pin = serializers.CharField(write_only=True, min_length=4, max_length=6)

    class Meta:
        model = CustomUser
        fields = ['phone', 'pin', 'confirm_pin']

    def validate(self, data):
        if data['pin'] != data['confirm_pin']:
            raise serializers.ValidationError("PINs do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_pin')
        user = CustomUser.objects.create_user(
            phone=validated_data['phone'],
            pin=validated_data['pin']
        )
        return user

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    pin = serializers.CharField(write_only=True)

class PinResetSerializer(serializers.Serializer):
    phone = serializers.CharField()
    new_pin = serializers.CharField(write_only=True, min_length=4, max_length=6)
    confirm_new_pin = serializers.CharField(write_only=True, min_length=4, max_length=6)

    def validate(self, data):
        if data['new_pin'] != data['confirm_new_pin']:
            raise serializers.ValidationError("New PINs do not match.")
        return data
