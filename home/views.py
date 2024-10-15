from django.shortcuts import render, HttpResponse, redirect
from . models import Question, Quiz, Answer, QuizSubmitted
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
import string 
import uuid 
import random 



# Create your views here.
def signup(request):
    if request.method=='POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['signupemail']
        password = request.POST['signuppassword1']
        password2 = request.POST['signuppassword2']

        # Checks for creating User
        if len(uname) < 3:
            messages.error(request, 'Username should be greater then 3')

        create_newuser = User.objects.create_user(uname, email, password2)
        create_newuser.first_name = fname
        create_newuser.last_name = lname
        create_newuser.save()
        messages.success(request, f'User {uname} created successfully, Go ahead and Login to your Account')

    return redirect('/')


def handle_login(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']    

        user = authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, f'Successfully Logged in as - {user}')
            return redirect('/')
        else:
            messages.error(request, 'No Such User exists')
            return redirect('/')
    else:
        messages.error(request, f'{user} Details dont Match the Database Please Try Agians')
        return redirect('/')


@login_required
def handle_logout(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    messages.success(request, f' Successfully Logged Out')
    return redirect('/')




# Create your views here.
def index(request):
    quiz = Quiz.objects.all()
    
    # if request.user:
    #     userSubmitted_Quiz = QuizSubmitted.objects.filter(userSubmitted=request.user)
    
    context = {"quiz" : quiz}
    return render(request, template_name='index.html', context=context)

@login_required
def open_quiz(request, quiz_id):
    quiz = Quiz.objects.get(quiz_id=quiz_id)
    que = Question.objects.all().filter(quiz=quiz_id)    
    context = {"quiz": quiz, "que" : que}
    print(context)
    return render(request, template_name="quiz_home.html", context=context)

@login_required
def submit(request):
    if request.method == "POST":
        current_quiz = request.POST.get('quiz_id')
        print(current_quiz)
        score = 0
        if int(current_quiz) > 0:
            questions = Question.objects.filter(quiz=current_quiz).values_list('question_id', flat=True)
            len_questions = len(questions)

            for i in questions:
                cur_question = i
                cur_choice = request.POST.get('choice' + str(i))
                cur_correct_choice = Question.objects.get(question_id=cur_question).correct_choice
                cur_choice_marks = Question.objects.get(question_id=cur_question).marks
                print("Current choice marks are : " + str(cur_choice_marks))

                # Saving the Answer
                if int(cur_choice) == int(cur_correct_choice):
                    isCorrect = True
                    finalMarks = cur_choice_marks
                else:
                    isCorrect = False
                    finalMarks = 0
                # isCorrect = (int(cur_choice) == int(cur_correct_choice)) ? True : False 
                # finalMarks = cur_choice_marks if isCorrect else 0
                score += finalMarks

                print("The Choice provided is " + str(cur_choice) + " and correct is " + str(cur_correct_choice))
                # print(isCorrect)
                ans = Answer(quiz=Quiz.objects.get(quiz_id=current_quiz), question=Question.objects.get(question_id=cur_question), answer=cur_choice, iscorrect=isCorrect, score=finalMarks)
                ans.save()
                print("Answer Saved Successfully")
                # print(cur_question, cur_choice)
            
            messages.success(request, f"Your Quiz has been submitted Successfully and your score is {score}")
        
            print("Current Quiz is", current_quiz)
            print(request.user.first_name)
            quiz_submit = QuizSubmitted(quiz=Quiz.objects.get(quiz_id=1), userSubmitted=request.user, score=score)
            quiz_submit.save()
        # print(quiz_submit)
        # print(submitted_quiz)
        # submitted_quiz.save()
            # submitted_quiz.save()
        # print(current_quiz)
        # print(request.POST.items)
        # print(type(request.POST.items))
        return redirect('/')


def about(request):
    return render(request, template_name="about.html")

def contact(request):
    return render(request, template_name="contact.html")