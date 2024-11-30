from datetime import datetime, timedelta

from django.conf import settings
from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    ForeignKey,
    CASCADE,
    UniqueConstraint,
)
from django.utils import timezone
from django.utils.crypto import get_random_string


def get_token() -> str:
    return get_random_string(64)


def get_created_at() -> datetime:
    return timezone.now()


def get_expired_at() -> datetime:
    return timezone.now() + timedelta(minutes=20)


class LoginToken(Model):
    token: str = CharField(max_length=64, default=get_token)
    created_at: datetime = DateTimeField(default=get_created_at)
    expired_at: datetime = DateTimeField(default=get_expired_at)
    user = ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=CASCADE
    )
    used_at: datetime = DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['token'],
                name='unique_login_token__token',
            ),
        ]
