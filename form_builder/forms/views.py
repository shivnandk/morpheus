from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response as RestResponse  # Alias to avoid conflict
from django.shortcuts import get_object_or_404, render
from collections import Counter
from .models import Form, Question, Answer, Response
from .serializers import FormSerializer, QuestionSerializer, AnswerSerializer, ResponseSerializer

# ViewSets for Form, Question, Answer, and Response models
class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

# Helper function to count and categorize common answers
def get_common_choices(all_answers, is_checkbox=False):
    all_choices = []
    if is_checkbox:
        all_choices = [choice for answer in all_answers for choice in (answer.answer_choice or [])]
    else:
        all_choices = [answer.answer_choice[0] for answer in all_answers if answer.answer_choice]
    
    choice_counts = Counter(all_choices)
    common_choices = choice_counts.most_common(5)
    others = sum([count for choice, count in choice_counts.items() if choice not in dict(common_choices)])
    return common_choices, others

# View to return analytics for a form (REST API)
@api_view(['GET'])
def get_form_analytics(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    responses = Response.objects.filter(form=form)
    
    analytics = {
        'form_title': form.title,
        'total_responses': responses.count(),
        'question_analytics': []
    }
    
    for question in form.questions.all():
        question_data = {
            'question_text': question.question_text,
            'question_type': question.question_type,
            'analytics': {}
        }
        
        if question.question_type == 'text':
            all_answers = Answer.objects.filter(question=question)
            text_answers = [answer.answer_text for answer in all_answers]
            word_counts = Counter([word for word in ' '.join(text_answers).split() if len(word) >= 5])
            common_words = word_counts.most_common(5)
            others = sum([count for word, count in word_counts.items() if word not in dict(common_words)])
            question_data['analytics'] = {
                'common_words': common_words,
                'others_count': others
            }

        elif question.question_type == 'checkbox':
            all_answers = Answer.objects.filter(question=question)
            common_choices, others = get_common_choices(all_answers, is_checkbox=True)
            question_data['analytics'] = {
                'common_choices': common_choices,
                'others_count': others
            }

        elif question.question_type == 'dropdown':
            all_answers = Answer.objects.filter(question=question)
            common_choices, others = get_common_choices(all_answers, is_checkbox=False)
            question_data['analytics'] = {
                'common_choices': common_choices,
                'others_count': others
            }
        
        analytics['question_analytics'].append(question_data)

    return RestResponse(analytics)

# View to render analytics in a tabular format
def render_form_analytics(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    responses = Response.objects.filter(form=form)
    
    analytics = {
        'form_title': form.title,
        'total_responses': responses.count(),
        'questions': []
    }
    
    for question in form.questions.all():
        question_data = {
            'question_text': question.question_text,
            'question_type': question.question_type,
            'analytics': {}
        }
        
        if question.question_type == 'text':
            all_answers = Answer.objects.filter(question=question)
            text_answers = [answer.answer_text for answer in all_answers]
            word_counts = Counter([word for word in ' '.join(text_answers).split() if len(word) >= 5])
            common_words = word_counts.most_common(5)
            question_data['analytics'] = {
                'type': 'text',
                'common_words': common_words
            }

        elif question.question_type == 'checkbox':
            all_answers = Answer.objects.filter(question=question)
            common_choices, _ = get_common_choices(all_answers, is_checkbox=True)
            question_data['analytics'] = {
                'type': 'checkbox',
                'common_choices': common_choices
            }

        elif question.question_type == 'dropdown':
            all_answers = Answer.objects.filter(question=question)
            common_choices, _ = get_common_choices(all_answers, is_checkbox=False)
            question_data['analytics'] = {
                'type': 'dropdown',
                'common_choices': common_choices
            }
        
        analytics['questions'].append(question_data)

    return render(request, 'forms/form_analytics.html', {'analytics': analytics})
