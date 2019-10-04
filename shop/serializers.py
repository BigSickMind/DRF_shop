from rest_framework.serializers import ModelSerializer

from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'surname',
            'name',
            'patronymic',
            'full_name',
            'email',
            'creation_date',
        ]
