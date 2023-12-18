from django.urls import path, include
from rest_framework import routers
from .views import LanguageViewSet, CardViewSet, ModuleCreateView, ModuleEditView, ModuleListView

router = routers.DefaultRouter()
router.register(r'cards', CardViewSet, basename='cards')
router.register(r'languages', LanguageViewSet, basename='languages')
router.register(r'list', ModuleListView, basename='modules_list')
router.register(r'edit', ModuleEditView, basename='modules_edit')
router.register(r'create', ModuleCreateView, basename='modules_create')


urlpatterns = [
    path('', include(router.urls)),
    # path('cards/modules/create/', ModuleCreateView.as_view()),
    # path('cards/modules/update/', ModuleEditView.as_view()),
    # path('cards/modules/list/', ModuleListView.as_view()),
]
