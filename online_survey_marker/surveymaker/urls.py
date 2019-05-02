from django.urls import path

from . import views

app_name = 'surveymaker'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/create',views.create, name='create'),
    path('<int:user_id>/surveys',views.DetailView.as_view(), name='sview'),
    path('<int:survey_id>/initQ',views.initQ, name='initQ'),
    path('<int:survey_id>/buildQ/<int:num_of_choice>/choice',views.buildQ, name='buildQ'),
]