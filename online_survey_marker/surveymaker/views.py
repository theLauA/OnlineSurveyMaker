from django.shortcuts import render,get_object_or_404
from .models import MCUser,MCQuestion,Survey
from django.views import generic
# Create your views here.

uid = 1
def index(request):
    user = MCUser.objects.get(pk=uid)
    context = {
        'user':user
    }
    return render(request,'smaker/index.html',context)

class MakeView(generic.DetailView):
    model = MCUser
    template_name = 'smaker/maker.html'

class DetailView(generic.ListView):
    template_name = 'smaker/survey.html'
    context_object_name = 'all_survey_set'

    def get_queryset(self):
        return MCUser.objects.get(pk=uid).survey_set.order_by('-pub_date')