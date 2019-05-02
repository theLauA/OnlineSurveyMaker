from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .models import MCUser,MCQuestion, MCChoice, Survey
from django.utils import timezone

class ViewsTests(TestCase):

    def setUp(self):
        
        user = MCUser(username="Barry",date_joined=timezone.now())
        user.save()
        self.user = user

    def createSurvey(self,user):
        #Setup database with one user with one survey with one choice
        survey = user.survey_set.create(survey_name="Dummy Survey",pub_date=timezone.now())
        survey.save()

        return survey
        
    def createQuestion(self,survey):
        question = survey.mcquestion_set.create(question_text="Dummy Question")
        question.save()

        return question

    def test_index_url_zero_survey(self):

        url = reverse('surveymaker:index')
        reponse = self.client.get(url)
        #reponse contain username
        return self.assertContains(reponse,"Barry")

    def test_ssview_url_zero_survey(self):

        url = reverse('surveymaker:ssview',args=(self.user.id,))
        reponse = self.client.get(url)
        #reponse contain place holder text
        return self.assertContains(reponse,"Dont Have Any Survey")

    def test_ssview_url_one_survey(self):
        self.createSurvey(user = self.user)
        url = reverse('surveymaker:ssview',args=(self.user.id,))
        reponse = self.client.get(url)
        #reponse contain place holder text
        return self.assertNotContains(reponse,"Dont Have Any Survey")

    def test_ssview_url_one_question(self):
        survey = self.createSurvey(user = self.user)
        self.createQuestion(survey = survey)
        url = reverse('surveymaker:sview',args=(survey.id,))
        reponse = self.client.get(url)
        #reponse contain place holder text
        return self.assertContains(reponse,"Dummy Question")

    def test_sview_url_invalid(self):
        url = reverse('surveymaker:sview',args=(20,))
        reponse = self.client.get(url)
        #reponse contain place holder text
        return self.assertEqual(reponse.status_code,404)



    
