from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser

class RegisterForm(forms.Form):
    phone = forms.CharField(max_length=15)
    pin = forms.CharField(max_length=6, widget=forms.PasswordInput)
    confirm_pin = forms.CharField(max_length=6, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        pin = cleaned_data.get("pin")
        confirm_pin = cleaned_data.get("confirm_pin")
        if pin != confirm_pin:
            raise ValidationError("PINs do not match.")
        return cleaned_data

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=15)
    pin = forms.CharField(max_length=6, widget=forms.PasswordInput)

class PinResetForm(forms.Form):
    phone = forms.CharField(max_length=15)
    new_pin = forms.CharField(max_length=6, widget=forms.PasswordInput)
    confirm_new_pin = forms.CharField(max_length=6, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_pin = cleaned_data.get("new_pin")
        confirm_new_pin = cleaned_data.get("confirm_new_pin")
        if new_pin != confirm_new_pin:
            raise ValidationError("New PINs do not match.")
        return cleaned_data
