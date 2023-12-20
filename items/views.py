from rest_framework import viewsets, permissions, generics, filters
from .serializers.common import ItemSerializer
from .serializers.specialized import ItemAndUsagesSerializer
from .models import Item, Profile


class IsOwnerOfItem(permissions.BasePermission):
    message = 'You are not a member of the account that owns this item.'

    def has_object_permission(self, request, view, obj):
        return obj.owner.account == request.user


class IsCreatorOfOwner(permissions.BasePermission):
    message = 'You are not a member of the account that created the item\'s owner\'s profile.'

    def has_permission(self, request, view):
        if request.method == 'POST':
            profile_id = request.data['owner']
            try:
                profile = Profile.objects.get(id=profile_id)
            except Profile.DoesNotExist:
                return False
            return profile.account == request.user
        return True


class ItemViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOfItem, IsCreatorOfOwner]

    def get_queryset(self):
        account = self.request.user
        return Item.objects.filter(owner__account=account)

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        if item.image:
            item.image.delete()
        return super().destroy(request, *args, **kwargs)


class ItemAndUsagesRetrieveView(generics.RetrieveAPIView):
    serializer_class = ItemAndUsagesSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOfItem]

    def get_queryset(self):
        item_id = self.kwargs['pk']
        return Item.objects.prefetch_related('usages').filter(id=item_id)
