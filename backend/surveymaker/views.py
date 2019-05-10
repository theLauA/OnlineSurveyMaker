from django.shortcuts import render,get_object_or_404
from .models import MCUser,MCQuestion,Survey,MCChoice
from rest_framework import generics
from .forms import NameForm,NumberForm,MCMakerForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets,status
from .serializers import UserSerializer,SurveySerializer,SurveyDetailSerializer,MCQuestionSerializer,MCChoiceSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = MCUser.objects.all()

class SurveysView(generics.ListAPIView):
    serializer_class = SurveySerializer
    
    def get_queryset(self):
        userid = self.kwargs['userid']
        return Survey.objects.filter(creater=userid)

class SurveyView(viewsets.ModelViewSet):
    serializer_class = SurveyDetailSerializer
    queryset = Survey.objects.all()

    
    def update(self,request,pk=None):
        survey = self.get_object()
        serializer = MCQuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = MCQuestion.objects.create(survey=survey,question_text=serializer.data['question_text'])
            for choice in request.data['choices']:
                c_serializer = MCChoiceSerializer(data=choice)
                if c_serializer.is_valid():
                    c = MCChoice.objects.create(question=question,choice_text=c_serializer.data['choice_text'])
                    c.save()
            question.save()
            return Response({'status':'question add'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)