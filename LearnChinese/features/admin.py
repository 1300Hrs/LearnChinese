from django.contrib import admin
from .models import Quiz, Question, Choice


class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question_text", "correct_answer")


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "choice_text")


# Register your models here.
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

