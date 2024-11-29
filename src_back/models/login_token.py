from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    ForeignKey,
    CASCADE,
    UniqueConstraint,
)
from django.utils import timezone


def get_created_at() -> datetime:
    return timezone.now()


def get_expired_at() -> datetime:
    return timezone.now() + timedelta(seconds=2.5 * 60)


class LoginToken(Model):
    token: str = CharField(max_length=255)
    created_at: datetime = DateTimeField(default=get_created_at)
    expired_at: datetime = DateTimeField(default=get_expired_at)
    user: User = ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
    used_at: datetime = DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["token"],
                name="unique_login_token__token",
            ),
        ]
