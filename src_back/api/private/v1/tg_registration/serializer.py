from rest_framework.serializers import Serializer, CharField


class UserSerializer(Serializer):
    username: str = CharField()
    first_name: str = CharField(required=False)
    last_name: str = CharField(required=False)
    external_id: str = CharField()


class TgRegistrationSerializer(Serializer):
    token: str = CharField()
    user_data: UserSerializer = UserSerializer()
