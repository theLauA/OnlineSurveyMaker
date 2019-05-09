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
        survey = user.survey_set.create(survey_name=surveyname,pub_date=timezone.now())
        survey.save()

        return survey
        
    def createQuestion(self,survey,question_text="Dummy Question"):
        # Create one Question under survey
        question = survey.mcquestion_set.create(question_text=question_text)
        question.save()

        return question

    def test_index_url_zero_survey(self):

        url = reverse('surveymaker:index')
        reponse = self.client.get(url)
        #Check If Index Page Retrieve the username
        return self.assertContains(reponse,"Barry")

    def test_ssview_url_zero_survey(self):
        url = reverse('surveymaker:ssview',args=(self.user.id,))
        reponse = self.client.get(url)
        #Test One Check If SurveysView has the right place holder.
        return self.assertContains(reponse,"Dont Have Any Survey")

    def test_ssview_url_zero_survey_alt(self):
        # Barry has no Survey but Dummy has one Survey
        user_dummy = self.createUser(self)
        self.createSurvey(user_dummy)
        url = reverse('surveymaker:ssview',args=(self.user.id,))
        reponse = self.client.get(url)
        #Test Two Check If SurveysView has the right place holder.
        return self.assertContains(reponse,"Dont Have Any Survey")

    def test_ssview_url_one_survey(self):
        self.createSurvey(user = self.user)
        url = reverse('surveymaker:ssview',args=(self.user.id,))
        reponse = self.client.get(url)
        #Check If SurveysView has the right Survey
        return self.assertContains(reponse,"Dummy Survey")

    def test_ssview_url_one_question(self):
        survey = self.createSurvey(user = self.user)
        self.createQuestion(survey = survey)
        url = reverse('surveymaker:sview',args=(survey.id,))
        reponse = self.client.get(url)
        #Check If SurveyView has the right Question
        return self.assertContains(reponse,"Dummy Question")

    def test_sview_url_invalid(self):
        # Simple Test for 404 response
        url = reverse('surveymaker:sview',args=(20,))
        reponse = self.client.get(url)
        return self.assertEqual(reponse.status_code,404)



    
