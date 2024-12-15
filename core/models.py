from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, pin, **extra_fields):
        if not phone:
            raise ValueError('Phone number must be provided.')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(pin)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, pin, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone, pin, **extra_fields)

class CustomUser(AbstractBaseUser):
    phone = models.CharField(max_length=15, unique=True)
    pin = models.CharField(max_length=6)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone
