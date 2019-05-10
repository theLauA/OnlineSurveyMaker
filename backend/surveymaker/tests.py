from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .models import MCUser,MCQuestion, MCChoice, Survey
from django.utils import timezone

class ViewsTests(TestCase):

    # For all Test Cases in ViewsTests
    def setUp(self):
        # Create One User
        user = MCUser(username="Barry",date_joined=timezone.now())
        user.save()
        self.user = user

    def createUser(self,username="Dummy"):
        #Create one User
        user = MCUser(username=username,date_joined=timezone.now())
        user.save()
        return user

    def createSurvey(self,user,surveyname="Dummy Survey"):
        # Create One Survey for user
        survey = Survey.objects.create(creater=user,survey_name=surveyname,pub_date=timezone.now())
        survey.save()

        return survey
        
    def createQuestion(self,survey,question_text="Dummy Question"):
        # Create one Question under survey
        question = MCQuestion.objects.create(survey=survey,question_text=question_text)
        question.save()

        return question

    def test_api_url_zero_survey(self):

        url = '/api/users/'
        reponse = self.client.get(url)
        return self.assertContains(reponse,"Barry")
    

    def test_api_url_one_survey(self):
        survey = self.createSurvey(user = self.user)
        url = '/api/users/'
        reponse = self.client.get(url)
        #Check If SurveysView has the right Survey
        return self.assertContains(reponse,"Dummy Survey")

    def test_api_url_one_question(self):
        survey = self.createSurvey(user = self.user)
        self.createQuestion(survey = survey)
        url = '/api/surveys/'
        reponse = self.client.get(url)
        #Check If SurveyView has the right Question
        return self.assertContains(reponse,"Dummy Question")

    def test_api_url_invalid(self):
        # Simple Test for 301 response
        url = '/api/surveys/'+str(200)
        reponse = self.client.get(url)
        return self.assertEqual(reponse.status_code,301)


    
    
