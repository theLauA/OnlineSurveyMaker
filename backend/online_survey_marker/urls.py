"""online_survey_marker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from surveymaker import views

router = routers.DefaultRouter()
router.register(r'users',views.UserView,'user')
router.register(r'surveys',views.SurveyView,'survey')


urlpatterns = [
    #path('smaker/',include('surveymaker.urls')),
    #path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/users/<int:userid>/surveys',views.SurveysView.as_view()),
    
]
