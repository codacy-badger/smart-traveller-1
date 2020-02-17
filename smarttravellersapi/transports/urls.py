from django.urls import path, include
from rest_framework import routers
from transports.views import (
    FleetTypeViewSet, FleetViewSet, LocationViewSet,
    RouteViewSet, FleetAssignmentViewSet
)

router = routers.DefaultRouter()
router.register('fleet-types', FleetTypeViewSet)
router.register('fleets', FleetViewSet)
router.register('locations', LocationViewSet)
router.register('routes', RouteViewSet)
router.register('fleet-assignments', FleetAssignmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
