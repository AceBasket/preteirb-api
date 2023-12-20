from rest_framework import serializers
from ..models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def remove_previous_item_image(self, instance, validated_data):
        if 'image' in validated_data and instance.image:
            instance.image.delete()

    def update(self, instance, validated_data):
        self.remove_previous_item_image(instance, validated_data)
        return super().update(instance, validated_data)
