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
from rest_framework.decorators import action
from rest_framework import status


class ItemViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # @action(detail=True, methods=['post', 'patch', 'put'])
    # def upload_item_image(self, request, pk=None):
    #     item = self.get_object()
    #     serializer = ItemSerializer(
    #         item, data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
