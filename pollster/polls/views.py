from django.shortcuts import render

# Create your views here.
from .models import Question, Choice

# Get Questions for display


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
