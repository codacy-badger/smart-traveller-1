from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from transports.serializers import (
    FleetTypeSerializer, FleetSerializer, LocationSerializer,
    RouteSerializer, FleetAssignmentSerializer
)
from transports.models import ( FleetType, Fleet,
    Location, Route, FleetAssignment
)

class FleetTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows create, retrieve, update and delete _
    operations be performed on a fleettype.
    """

    queryset = FleetType.objects.all().order_by('id')
    serializer_class = FleetTypeSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'retrieve':
            permission_classes = [IsAdminUser]

        if self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]

class FleetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows create, retrieve, update and delete _
    operations be performed on a fleet.
    """

    queryset = Fleet.objects.all().order_by('id')
    serializer_class = FleetSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'retrieve':
            permission_classes = [IsAdminUser]

        if self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows create, retrieve, update and delete _
    operations be performed on a location.
    """

    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'retrieve':
            permission_classes = [IsAdminUser]

        if self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]


class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows create, retrieve, update and delete _
    operations be performed on a route.
    """

    queryset = Route.objects.all().order_by('id')
    serializer_class = RouteSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'retrieve':
            permission_classes = [IsAdminUser]

        if self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]


class FleetAssignmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows create, retrieve, update and delete _
    operations be performed on a fleetassignment.
    """

    queryset = FleetAssignment.objects.all().order_by('id')
    serializer_class = FleetAssignmentSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'retrieve':
            permission_classes = [IsAdminUser]

        if self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsLoggedInUserOrAdmin]

        if self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]
