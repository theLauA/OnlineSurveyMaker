from django.shortcuts import render,get_object_or_404
from .models import MCUser,MCQuestion,Survey
from rest_framework import generics
from .forms import NameForm,NumberForm,MCMakerForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from .serializers import UserSerializer,SurveySerializer,SurveyDetailSerializer
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