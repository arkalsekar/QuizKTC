from django.shortcuts import render, HttpResponse
from . models import Question, Quiz, Answer

# Create your views here.
def index(request):
    quiz = Quiz.objects.all()
    context = {"quiz" : quiz}
    return render(request, template_name='index.html', context=context)

def open_quiz(request, quiz_id):
    quiz = Quiz.objects.get(quiz_id=quiz_id)
    que = Question.objects.all().filter(question_id=quiz_id)    
    context = {"quiz": quiz, "que" : que}
    # print(context)
    return render(request, template_name="quiz_home.html", context=context)


def about(request):
    return render(request, template_name="about.html")

def contact(request):
    return render(request, template_name="contact.html")