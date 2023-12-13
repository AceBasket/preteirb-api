from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers.common import ItemSerializer
from .serializers.specialized import ItemAndUsagesSerializer
from .models import Item
from usages.models import Usage


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request):
        queryset = request.user.items.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)


# class ItemAndUsagesViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = ItemAndUsagesSerializer

#     def get_queryset(self):
#         item_id = self.kwargs['id']
#         return Item.objects.prefetch_related('usages').filter(id=item_id)

class ItemAndUsagesRetrieveView(generics.RetrieveAPIView):
    serializer_class = ItemAndUsagesSerializer

    def get_queryset(self):
        item_id = self.kwargs['pk']
        return Item.objects.prefetch_related('usages').filter(id=item_id)
