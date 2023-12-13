from rest_framework import serializers
from items.serializers.common import ItemSerializer
from ..models import Profile
from items.models import Item


class ItemsOwnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
