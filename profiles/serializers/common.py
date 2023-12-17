from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def remove_previous_profile_pic(self, instance, validated_data):
        pic = validated_data['profile_pic']
        if instance.profile_pic:
            instance.profile_pic.delete()

    def update(self, instance, validated_data):
        self.remove_previous_profile_pic(instance, validated_data)
        return super().update(instance, validated_data)
