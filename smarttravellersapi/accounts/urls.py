from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet, AgentViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('agents', AgentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls'))
]