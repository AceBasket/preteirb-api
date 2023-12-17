from django.contrib.auth import get_user_model
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password',
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
            }
        }
