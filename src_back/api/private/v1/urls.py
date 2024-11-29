from django.urls import path

from src_back.api.private.v1.tg_registration.view import TgRegistrationAPIView

urlpatterns = [
    path("tgRegistration", TgRegistrationAPIView.as_view()),
]
