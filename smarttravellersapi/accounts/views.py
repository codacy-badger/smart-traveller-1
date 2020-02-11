from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.serializers import UserSerializer
from accounts.models import CustomUser
from accounts.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [AllowAny]
        
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated]
        
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
