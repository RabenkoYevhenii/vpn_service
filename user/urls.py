from django.urls import path
from user.views import register, login_view

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
]

app_name = "user"
