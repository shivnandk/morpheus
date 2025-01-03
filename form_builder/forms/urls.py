from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FormViewSet, QuestionViewSet, AnswerViewSet, ResponseViewSet

router = DefaultRouter()
router.register(r'forms', FormViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
