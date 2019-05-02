from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .models import MCUser,MCQuestion, MCChoice, Survey
from django.utils import timezone
class ViewsTests(TestCase):

    def setUp(self):
        #Setup database with one user with one survey with one choice
        user = MCUser(username="Barry",date_joined=timezone.now())
        user.save()
        survey = user.survey_set.create(survey_name="Dummy Survey",pub_date=timezone.now())
        survey.save()
        question = question.survey_set.create(question_text="Dummy Question",pub_date=timezone.now())

    def test_index_url(self):
        url = reverse('surveymaker:index')
        reponse = self.client.get(url)
        #Should return one user
        return self.assertContains(reponse,"Barry")

    
