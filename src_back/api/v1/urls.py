from django.urls import path

from src_back.api.v1.login.view import OverrideLoginView

urlpatterns = [
    path("login", OverrideLoginView.as_view()),
]
