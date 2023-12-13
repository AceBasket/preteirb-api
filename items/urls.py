from rest_framework import routers
from django.urls import path, include
from .views import ItemViewSet, ItemAndUsagesRetrieveView
from .models import Item


router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
# router.register(r'items/(?P<id>\d+)/usages',
#                 ItemAndUsagesRetrieveView, basename='item-usages')

urlpatterns = [
    path('', include(router.urls)),
    path('items/<int:pk>/usages/', ItemAndUsagesRetrieveView.as_view()),
]
