from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FormViewSet, 
    QuestionViewSet, 
    AnswerViewSet, 
    ResponseViewSet, 
    get_form_analytics, 
    render_form_analytics
)

# Register API viewsets
router = DefaultRouter()
router.register(r'forms', FormViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
    path('analytics/<int:form_id>/', get_form_analytics, name='form_analytics'),  # API analytics URL
    path('analytics/table/<int:form_id>/', render_form_analytics, name='render_form_analytics'),  # Tabular view URL
]
