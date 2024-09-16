from django.shortcuts import render, redirect
from .models import Question, QuizResult
from django.contrib.auth.decorators import login_required

def quiz_home(request):
    questions = Question.objects.all()
    return render(request, 'quiz/home.html', {'questions': questions})

@login_required
def submit_quiz(request):
    if request.method == 'POST':
        user = request.user
        score = 0
        questions = Question.objects.all()
        for question in questions:
            correct_answer = question.correct_option
            selected_answer = request.POST.get(str(question.id))
            if selected_answer == correct_answer:
                score += 1
        QuizResult.objects.create(user=user, score=score)
        return redirect('quiz:result', score=score)
    return redirect('quiz:home')

def quiz_result(request, score):
    return render(request, 'quiz/result.html', {'score': score})

from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

