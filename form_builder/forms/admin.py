from django.contrib import admin
from .models import Form, Question, Answer, Response

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')  # Display form ID, title, and creation date
    inlines = [QuestionInline]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'response', 'question', 'answer_text', 'answer_choice')  # Display answer ID, response ID, question ID, answer text, and choice

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'form', 'created_at')  # Display response ID, form ID, and creation date

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'form', 'question_type', 'order')  # Display question ID, question text, form ID, question type, and order

# Register models with the admin panel
admin.site.register(Form, FormAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Response, ResponseAdmin)
