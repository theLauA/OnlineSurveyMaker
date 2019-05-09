from rest_framework import serializers
from .models import MCUser,Survey,MCQuestion,MCChoice

class MCChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCChoice
        fields = ('id','choice_text','question')

class MCQuestionSerializer(serializers.ModelSerializer):
    choices = MCChoiceSerializer(many=True,read_only=True)
    class Meta:
        model = MCQuestion
        fields = ('id','question_text','choices','survey')

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id','survey_name')

class UserSerializer(serializers.ModelSerializer):
    surveys = SurveySerializer(many=True, read_only=True)
    class Meta:
        model = MCUser
        fields = ('id', 'username', 'date_joined','surveys')

class SurveyDetailSerializer(serializers.ModelSerializer):
    questions = MCQuestionSerializer(many=True,read_only=True)
    class Meta:
        model = Survey
        fields = ('id','creater','survey_name','pub_date','questions')
