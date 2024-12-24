from django.urls import path
from .views import RegisterView, LoginView, PinResetView, HomeView


urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('pin-reset/', PinResetView, name='pin-reset'),
    path('home/', HomeView, name='home'),
]