from rest_framework import routers
from django.urls import path, include
from .views import UsageViewSet

router = routers.DefaultRouter()
router.register(r'usages', UsageViewSet, basename='usages')

urlpatterns = [
    path('', include(router.urls)),
]
