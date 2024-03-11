from rest_framework import serializers
from .models import Student


class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    
class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    