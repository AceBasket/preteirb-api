from rest_framework import viewsets, permissions
from .models import Usage, Item, Profile
from .serializers.common import UsageSerializer


class IsCreatorOfUsage(permissions.BasePermission):
    message = 'You are not a member of the account that created this usage.'

    def has_object_permission(self, request, view, obj):
        return obj.user.account == request.user


class IsOwnerOfItemAndCreatorOfProfile(permissions.BasePermission):
    message = 'You are not a member of the account that owns this item.'

    def has_permission(self, request, view):
        if request.method == 'POST':
            item_id = request.data['item']
            profile_id = request.data['user']
            try:
                item = Item.objects.get(id=item_id)
                profile = Profile.objects.get(id=profile_id)
            except (Item.DoesNotExist, Profile.DoesNotExist):
                return False
            return item.owner.account == request.user and profile.account == request.user
        return True


class UsageViewSet(viewsets.ModelViewSet):
    serializer_class = UsageSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsCreatorOfUsage, IsOwnerOfItemAndCreatorOfProfile]

    def get_queryset(self):
        account = self.request.user
        return Usage.objects.filter(user__account=account)
