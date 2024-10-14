from django.shortcuts import render, HttpResponse
from . models import Question, Quiz, Answer, SubmittedQuiz

# Create your views here.
def index(request):
    quiz = Quiz.objects.all()
    context = {"quiz" : quiz}
    return render(request, template_name='index.html', context=context)

def open_quiz(request, quiz_id):
    quiz = Quiz.objects.get(quiz_id=quiz_id)
    que = Question.objects.all().filter(quiz=quiz_id)    
    context = {"quiz": quiz, "que" : que}
    print(context)
    return render(request, template_name="quiz_home.html", context=context)

def submit(request):
    if request.method == "POST":
        current_quiz = request.POST.get('quiz_id')
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
                isCorrect = True if (int(cur_choice) == int(cur_correct_choice)) else False 
                finalMarks = cur_choice_marks if isCorrect else 0
                score += finalMarks

                print("The Choice provided is " + str(cur_choice) + " and correct is " + str(cur_correct_choice))
                print(isCorrect)
                ans = Answer(quiz=Quiz.objects.get(quiz_id=current_quiz), question=Question.objects.get(question_id=cur_question), answer=cur_choice, iscorrect=isCorrect, score=finalMarks)
                ans.save()
                print("Answer Saved Successfully")
                # print(cur_question, cur_choice)
        
            submitted_quiz = SubmittedQuiz(quiz=Quiz.objects.get(quiz_id=current_quiz), score=score)
            submitted_quiz.save()
        # print(current_quiz)
        # print(request.POST.items)
        # print(type(request.POST.items))
        return HttpResponse("Success")


def about(request):
    return render(request, template_name="about.html")

def contact(request):
    return render(request, template_name="contact.html")