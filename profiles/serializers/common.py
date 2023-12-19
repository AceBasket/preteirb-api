from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['account']

    def remove_previous_profile_pic(self, instance, validated_data):
        pic = validated_data['profile_pic']
        if instance.profile_pic:
            instance.profile_pic.delete()

    def update(self, instance, validated_data):
        self.remove_previous_profile_pic(instance, validated_data)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['account'] = user
        return super().create(validated_data)
