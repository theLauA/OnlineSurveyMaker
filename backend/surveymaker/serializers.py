from rest_framework import serializers
from .models import MCUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCUser
        fields = ('id', 'username', 'date_joined')