from rest_framework import serializers
from .models import MCUser,Survey

class UserSerializer(serializers.ModelSerializer):
    surveys = serializers.StringRelatedField(many=True)
    class Meta:
        model = MCUser
        fields = ('id', 'username', 'date_joined','surveys')

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id','creater','survey_name','pub_date')

