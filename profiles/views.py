from django.db.models import Q
from rest_framework import viewsets, permissions
from items.models import Item
from usages.models import Usage
from .serializers.common import ProfileSerializer
from usages.serializers.specialized import UsageAndItemWithOwnerSerializer
from items.serializers.common import ItemSerializer
from usages.views import IsCreatorOfUsage, IsOwnerOfItemAndCreatorOfProfile
from items.views import IsOwnerOfItem, IsCreatorOfOwner


class IsCreatorOfProfile(permissions.BasePermission):
    message = 'You are not a member of the account that created this profile.'

    def has_object_permission(self, request, view, obj):
        return obj.account == request.user


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsCreatorOfProfile]

    def get_queryset(self):
        return self.request.user.profiles.all()

    def destroy(self, request, *args, **kwargs):
        # destroy profile_pic first
        profile = self.get_object()
        if profile.profile_pic:
            profile.profile_pic.delete()
        return super().destroy(request, *args, **kwargs)


class ProfileAndItemsOwnedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsCreatorOfProfile, IsOwnerOfItem]

    def get_queryset(self):
        profile_id = self.kwargs['id']
        return Item.objects.filter(owner__id=profile_id)


class UsageAndItemWithOwnerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UsageAndItemWithOwnerSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOfItemAndCreatorOfProfile, IsCreatorOfUsage]

    def get_queryset(self):
        # doesn't retrieve the items owned by the profile
        profile_id = self.kwargs['id']
        return Usage.objects.filter(user__id=profile_id).filter(~Q(item__owner__id=profile_id))
