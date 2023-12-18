from djoser.views import TokenDestroyView, TokenCreateView
from django.urls import path, include
from rest_framework import routers
from .views import CustomUserView, CreateCustomUserView
import djoser


router = routers.DefaultRouter()
router.register(r'register', CreateCustomUserView, basename='user_create')
router.register(r'info', CustomUserView, basename='user_create')

urlpatterns = [
    path('', include(router.urls)),
    path('token/create/', djoser.views.TokenCreateView.as_view(), name='token_create'),
    path('token/destroy', TokenDestroyView.as_view(), name='token_destroy')
]
