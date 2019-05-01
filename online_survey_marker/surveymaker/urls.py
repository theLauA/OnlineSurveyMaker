from django.urls import path

from . import views

app_name = 'surveymaker'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/make',views.MakeView.as_view(), name='make'),
    path('<int:user_id>/surveys',views.DetailView.as_view(), name='sview'),
]