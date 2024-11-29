from rest_framework.serializers import Serializer, CharField


class CheckLoginSerializer(Serializer):
    token: str = CharField()
