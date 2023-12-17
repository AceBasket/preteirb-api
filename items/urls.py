from rest_framework import routers
from django.urls import path, include
from .views import ItemViewSet, ItemAndUsagesRetrieveView
from .models import Item


router = routers.DefaultRouter()
router.register(r'items', ItemViewSet, basename='items')
urlpatterns = [
    path('', include(router.urls)),
    path('items/<int:pk>/usages/', ItemAndUsagesRetrieveView.as_view()),
]
