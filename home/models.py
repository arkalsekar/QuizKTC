from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz_id = models.IntegerField(primary_key=True, auto_created=True)
    quiz_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_created=True, null=True, blank=True)
    
    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    question_id = models.ForeignKey(Quiz, related_name='quiz',on_delete= models.CASCADE)
    question_str = models.CharField(blank=True, null=True, max_length=255)  
    marks = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return self.question_str
    
class Answer(models.Model):
    answer_id = models.ForeignKey(Question, related_name='question', on_delete= models.CASCADE)
    answer_option = models.CharField(null=True, blank=True, max_length=255)
    is_correct = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.answer_id 
    