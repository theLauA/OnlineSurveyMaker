from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .models import MCUser,MCQuestion, MCChoice, Survey
from django.utils import timezone
class ViewTests(TestCase):

    def setUp(self):
        user = MCUser(username="Barry",date_joined=timezone.now())
        user.save()

    def test_index_url(self):
        url = reverse('surveymaker:index')
        reponse = self.client.get(url)
        #Should return one user
        return self.assertContains(reponse,"Barry")
