from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'avatar']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar', 'bio']

