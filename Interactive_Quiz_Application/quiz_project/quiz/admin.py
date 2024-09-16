from django.contrib import admin
from .models import Question, Option, QuizResult

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(QuizResult)

