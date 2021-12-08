from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': 'Select a valid choice'
            })

    choice.votes += 1
    choice.save()

    return HttpResponseRedirect(reverse('polls:results',
            args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    winner_choice = question.choice_set.order_by('-votes').first()

    return render(request, 'polls/results.html', {
            'question': question,
            'winner': winner_choice
        })
