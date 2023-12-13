from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers.common import ItemSerializer
from .serializers.specialized import ItemAndUsagesSerializer
from .models import Item
from usages.models import Usage
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import filters


class ItemViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemAndUsagesRetrieveView(generics.RetrieveAPIView):
    serializer_class = ItemAndUsagesSerializer

    def get_queryset(self):
        item_id = self.kwargs['pk']
        return Item.objects.prefetch_related('usages').filter(id=item_id)
