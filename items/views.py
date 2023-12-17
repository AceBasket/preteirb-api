from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers.common import ItemSerializer
from .serializers.specialized import ItemAndUsagesSerializer
from .models import Item
from rest_framework import filters


class ItemViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ItemSerializer

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

    def get_queryset(self):
        item_id = self.kwargs['pk']
        return Item.objects.prefetch_related('usages').filter(id=item_id)
