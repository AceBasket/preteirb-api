from rest_framework import serializers
from items.serializers.common import ItemSerializer
from items.serializers.specialized import ItemWithOwnerSerializer
from profiles.serializers.common import ProfileSerializer
from ..models import Usage


class UsageAndItemWithOwnerSerializer(serializers.ModelSerializer):
    item = ItemWithOwnerSerializer()

    class Meta:
        model = Usage
        fields = '__all__'
