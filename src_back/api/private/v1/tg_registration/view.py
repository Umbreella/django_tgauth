from typing import Type

from django.utils import timezone
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from src_back.api.private.v1.tg_registration.serializer import (
    TgRegistrationSerializer,
)
from src_back.models import LoginToken, User


class TgRegistrationAPIView(CreateAPIView):
    permission_classes: tuple[BasePermission] = (AllowAny,)

    serializer_class: Type[Serializer] = TgRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer: TgRegistrationSerializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        token: str = serializer.validated_data['token']

        if login_token := LoginToken.objects.select_for_update(
            token=token,
            user__isnull=True,
        ).first():
            user: User = User.objects.create_user(
                provider='tg',
                **serializer.validated_data['user_data'],
            )

            login_token.user = user
            login_token.used_at = timezone.now()
            login_token.save(update_fields=['user', 'used_at'])

        return Response(data={})
