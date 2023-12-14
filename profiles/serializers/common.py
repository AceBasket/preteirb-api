from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def removed_previous_profile_pic(self, instance, validated_data):
        pic = validated_data.pop('profile_pic')
        if pic and instance.profile_pic:
            instance.profile_pic.delete()

    def update(self, instance, validated_data):
        self.removed_previous_profile_pic(instance, validated_data)
        return super().update(instance, validated_data)
