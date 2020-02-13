from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.serializers import UserSerializer, AgentSerializer
from accounts.models import CustomUser, Agent
from accounts.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows create, retrieve, update and delete _
    operations be performed on an user.
    """

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [AllowAny]

        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]

        if self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated]

        if self.action == 'list':
            permission_classes = [IsAuthenticated]

        if self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]

class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows create, retrieve, update and delete _
    operations be performed on an agent.
    """

    queryset = Agent.objects.all().order_by('id')
    serializer_class = AgentSerializer

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
