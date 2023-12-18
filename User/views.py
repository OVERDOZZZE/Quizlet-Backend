from rest_framework.viewsets import GenericViewSet
from .serializers import CustomUserSerializer, CreateCustomUserSerializer
from .models import CustomUser
from rest_framework import mixins
from Card.permissions import IsOwnerOrReadOnly


class CreateCustomUserView(
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer


class CustomUserView(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = CustomUser
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]
