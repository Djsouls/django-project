from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
    questions = Question.objects.order_by('pub_date')[:5]

    return render(request, 'polls/index.html', 
                {'latest_questions': questions}
            )


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'polls/detail.html', {'question': question})


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
