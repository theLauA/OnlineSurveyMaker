from django.shortcuts import render,get_object_or_404
from .models import MCUser,MCQuestion,Survey

from .forms import NameForm,NumberForm,MCMakerForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from .serializers import UserSerializer
# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = MCUser.objects.all()