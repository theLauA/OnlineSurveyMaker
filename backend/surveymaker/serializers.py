from rest_framework import serializers
from .models import MCUser,Survey

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCUser
        fields = ('id', 'username', 'date_joined')

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id','creater','survey_name','pub_date')