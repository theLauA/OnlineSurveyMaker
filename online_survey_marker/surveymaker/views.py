from django.shortcuts import render,get_object_or_404
from .models import MCUser,MCQuestion,Survey
from django.views import generic
from .forms import NameForm,NumberForm,MCMakerForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

uid = 1
def index(request):
    user = MCUser.objects.get(pk=uid)
    context = {
        'user':user
    }
    return render(request,'smaker/index.html',context)

def create(request, user_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
            survey_name = form.cleaned_data['your_name']
            user = MCUser.objects.get(pk=user_id)
            survey = user.survey_set.create(survey_name=survey_name,pub_date=timezone.now())
            context = {
                'all_survey_set':[survey],
                'form': NumberForm()
            }

            return HttpResponseRedirect(reverse('surveymaker:initQ',args=(survey.id,)))
            #return render(request,'smaker/builder.html',context)
    # if a GET (or any other method) we'll create a blank form
    
    form = NameForm()
    context = {
        'form': form
    }
    return render(request,'smaker/maker.html',context)

def initQ(request,survey_id):
    survey = Survey.objects.get(pk=survey_id)

    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            num_of_choice = form.cleaned_data['your_number']
            #Go to buildQ to build the questions and choices
            return HttpResponseRedirect(reverse('surveymaker:buildQ',args=(survey.id,num_of_choice,)))
    
    context = {
                'survey':survey,
                'form': NumberForm(),
                'sid': survey_id
            }
    return render(request,'smaker/builder.html',context)

def buildQ(request,survey_id,num_of_choice):
    survey = Survey.objects.get(pk=survey_id)

    if request.method == 'POST':
        form = MCMakerForm(num_of_choice,request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question_text']
            question = survey.mcquestion_set.create(question_text=question_text)
            for idx in range(num_of_choice):
                question.mcchoice_set.create(choice_text=form.cleaned_data['choice_'+str(idx)])

            return HttpResponseRedirect(reverse('surveymaker:initQ',args=(survey.id,)))

    
    context = {
        'form':MCMakerForm(num_of_choice=num_of_choice),
        'sid': survey_id,
        'nc': num_of_choice
    }

    return render(request,'smaker/mcbuilder.html',context)

class SurveysView(generic.ListView):
    template_name = 'smaker/survey_list.html'
    context_object_name = 'all_survey_set'

    def get_queryset(self):
        return MCUser.objects.get(pk=uid).survey_set.order_by('-pub_date')

class SurveyView(generic.DetailView):
    model = Survey
    template_name = 'smaker/survey_inactive.html'