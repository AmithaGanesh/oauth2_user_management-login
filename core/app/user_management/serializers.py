from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User

from rest_framework import serializers
from .models import CustomUser

class registerserializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['email']:
            if CustomUser.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('Email already exists. Please try logging in.')
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
