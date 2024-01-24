from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "password", "first_name", "last_name"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "password", "first_name", "last_name"]


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "password"]
