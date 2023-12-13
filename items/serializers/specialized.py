from rest_framework import serializers
from ..models import Item
from usages.serializers.common import UsageSerializer


class ItemAndUsagesSerializer(serializers.ModelSerializer):
    usages = UsageSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


# class ItemAndUsagesSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=500)
#     owner = serializers.IntegerField()
#     usages = UsageSerializer(many=True, read_only=True)
