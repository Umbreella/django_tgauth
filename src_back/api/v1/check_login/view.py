from typing import Type, Optional

from django.contrib.auth import login
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import BasePermission, AllowAny
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from src_back.api.v1.check_login.serializer import CheckLoginSerializer
from src_back.models import LoginToken


class CheckLoginAPIView(CreateAPIView):
    permission_classes: tuple[BasePermission] = (AllowAny,)

    serializer_class: Type[Serializer] = CheckLoginSerializer

    def create(self, request, *args, **kwargs) -> HttpResponse:
        serializer: CheckLoginSerializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        token: str = serializer.validated_data['token']

        login_token: Optional[LoginToken] = (
            LoginToken.objects.select_for_update()
            .filter(
                token=token,
                expired_at__gt=timezone.now(),
            )
            .first()
        )

        if not login_token:
            raise ValidationError('not valid token')

        response: HttpResponse

        if login_token.user:
            login(request, login_token.user)
            login_token.expired_at = timezone.now()
            response = Response(data={'redirect_url': '/'})
        else:
            response = Response()

        login_token.save(update_fields=['expired_at'])

        return response
