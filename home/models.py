from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
class Quiz(models.Model):
    quiz_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=100, blank=True, null=True)
    marks = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    CHOICES = (
    (1, 'First'),
    (2, 'Second'),
    (3, 'Third'),
    (4, 'Fourth'),)
    quiz = models.ForeignKey(Quiz, related_name="quiz", on_delete=models.CASCADE)
    question_id = models.BigAutoField(primary_key=True)
    question = models.CharField(blank=True, null=True, max_length=255)  
    choice1 = models.CharField(max_length=255, blank=True, null=True)
    choice2 = models.CharField(max_length=255, blank=True, null=True)
    choice3 = models.CharField(max_length=255, blank=True, null=True)
    choice4 = models.CharField(max_length=255, blank=True, null=True)
    correct_choice = models.IntegerField(null=True, blank=True, choices=CHOICES)
    marks = models.IntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return self.question
    
class Answer(models.Model):
    CHOICES = (
    (1, 'First'),
    (2, 'Second'),
    (3, 'Third'),
    (4, 'Fourth'),)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(choices=CHOICES, null=True, blank=True)
    iscorrect = models.BooleanField(default=False, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.quiz.name

# Model for Submitted Quiz
class QuizSubmitted(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    userSubmitted = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.userSubmitted)