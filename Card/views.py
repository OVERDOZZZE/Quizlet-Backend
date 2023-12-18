from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Card, Language, Module
from .serializers import ModuleSerializer, LanguageSerializer, CardSerializer
from .permissions import IsOwnerOrNone, IsOwnerOrReadOnly
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ModuleCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ModuleListView(
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(author=user)


class ModuleEditView(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsOwnerOrNone]


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = []


def start(request):
    return render(request, 'card/index.html')
