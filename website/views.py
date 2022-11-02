from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from question.models import generate_question, Question

def welcome(request):
    return HttpResponse("Welcome to the NBA website!")

def question(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        print(request.POST)
        print('answer is', answer)
        question_id = request.POST.get('question_id')
        q = get_object_or_404(Question, pk=question_id)
        request.session['question'] = q.question
        request.session['player1'] =  f'{q.player1_name} : {q.player1_count}'
        request.session['player2'] =  f'{q.player2_name} : {q.player2_count}'
        request.session['correct'] =  "Correct" if answer == q.answer else "Incorrect"
        if request.session.get('score') is None:
            request.session['score'] = 0
        if answer == q.answer:
            request.session['score'] += 1
        else:
            request.session['score'] = 0
            return redirect('/incorrect')
        
        return redirect('/result')
    
    else:
        q = generate_question()
        q.save()
        d = {
			"question" : q.question,
			"player1_name" : q.player1_name,
			"player2_name" : q.player2_name,
			"score" : request.session.get('score'),
			"question_id" : q.id,
		}
        return render(request, 'question.html', d)


def questions(request):
    questions = Question.objects.all()
    print(questions)
    return render(request, 'questions.html', {'questions': questions})

def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        return redirect('/question')
    print(request.GET)
    print(request.session.get('question'))
    d = {
       "question" : request.session.get('question'),
       "player1" : request.session.get('player1'),
       "player2" : request.session.get('player2'),
       "correct" : request.session.get('correct'),
       "score" : request.session.get('score')
    }
    print(d)
    return render(request, 'result.html', d)

def incorrect(request):
    if request.method == 'POST':
        return redirect('/question')
    print(request.GET)
    print(request.session.get('question'))
    d = {
       "question" : request.session.get('question'),
       "player1" : request.session.get('player1'),
       "player2" : request.session.get('player2'),
       "correct" : request.session.get('correct'),
       "score" : request.session.get('score')
    }
    print(d)
    return render(request, 'incorrect.html', d)

def about(request):
    context = {}
    return render(request, "about.html", context)
