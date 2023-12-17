from django.shortcuts import render
from rest_framework import viewsets
from .models import Usage
from .serializers.common import UsageSerializer
from .serializers.specialized import UsageAndItemWithOwnerSerializer


class UsageViewSet(viewsets.ModelViewSet):
    serializer_class = UsageSerializer

    def get_queryset(self):
        account = self.request.user
        return Usage.objects.filter(user__account=account)
