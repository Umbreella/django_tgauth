from django.urls import path

from src_back.api.v1.check_login.view import CheckLoginAPIView

urlpatterns = [
    path('checkLogin', CheckLoginAPIView.as_view()),
]
