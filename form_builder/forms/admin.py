from django.contrib import admin
from .models import Form, Question, Answer, Response

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class FormAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [QuestionInline]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_text', 'answer_choice')

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('form', 'created_at')

admin.site.register(Form, FormAdmin)
admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Response, ResponseAdmin)
