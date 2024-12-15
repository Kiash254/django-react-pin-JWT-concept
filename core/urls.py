from django.urls import path
from .views import RegisterView, LoginView, PinResetView, HomeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('pin-reset/', PinResetView.as_view(), name='pin_reset'),
    path('home/', HomeView.as_view(), name='home'),
]
