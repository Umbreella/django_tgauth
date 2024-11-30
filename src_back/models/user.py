from django.contrib.auth import models
from django.db.models import CharField


class User(models.AbstractUser):
    provider: str = CharField(max_length=255, blank=True)
    external_id: str = CharField(max_length=255, blank=True)
