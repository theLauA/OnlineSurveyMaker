from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

class MCUser(models.Model):
    username = models.CharField(max_length=200)
    date_joined = models.DateField()
    def __str__(self):
        return self.username

class Survey(models.Model):
    creater = models.ForeignKey(MCUser,on_delete=models.CASCADE)
    survey_name = models.CharField(max_length=200)
    pub_date = models.DateField()
    def __str__(self):
        return self.survey_name
    
class MCQuestion(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    
class MCChoice(models.Model):
    question= models.ForeignKey(MCQuestion,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

