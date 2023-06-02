from django.urls import path
from .views import LoginView, SignUpView, LogOutView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("get-api-token/", obtain_auth_token),
]
