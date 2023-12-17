from django.db.models import Q
from rest_framework import viewsets,
from items.models import Item
from usages.models import Usage
from .serializers.common import ProfileSerializer
from usages.serializers.specialized import UsageAndItemWithOwnerSerializer
from items.serializers.common import ItemSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

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

    def get_queryset(self):
        profile_id = self.kwargs['id']
        return Item.objects.filter(owner__id=profile_id)


class UsageAndItemWithOwnerViewSet(viewsets.ReadOnlyModelViewSet):
    # doesn't retrieve the items owned by the profile
    serializer_class = UsageAndItemWithOwnerSerializer

    def get_queryset(self):
        profile_id = self.kwargs['id']
        return Usage.objects.filter(user__id=profile_id).filter(~Q(item__owner__id=profile_id))
