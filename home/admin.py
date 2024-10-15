from django.contrib import admin
from .models import Question, Quiz, Answer, QuizSubmitted


admin.site.site_header = 'QuizKTC Admin Panel'
admin.site.index_title = 'Manage Your Datab ases'            
# admin.site.site_title = 'HTML title from adminsitration' 

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizSubmitted)