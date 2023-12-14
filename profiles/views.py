from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Profile
from items.models import Item
from usages.models import Usage
from .serializers.common import ProfileSerializer
from usages.serializers.specialized import UsageAndItemWithOwnerSerializer
from items.serializers.common import ItemSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser, FormParser]

    @action(detail=True, methods=['post', 'patch', 'put'])
    def upload_profile_picture(self, request, pk=None):
        user = self.get_object()
        serializer = ProfileSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        # usage__user__id=profile_id and usage__item__owner__id!=profile_id
        return Usage.objects.filter(user__id=profile_id).filter(~Q(item__owner__id=profile_id))
