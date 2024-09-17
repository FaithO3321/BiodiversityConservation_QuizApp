from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet
app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_home, name='home'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
    path('result/<int:score>/', views.quiz_result, name='result'),
]

router = DefaultRouter()
router.register(r'api/questions', QuestionViewSet)

urlpatterns += router.urls
