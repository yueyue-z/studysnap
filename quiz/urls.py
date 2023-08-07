from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path("", views.QuizHomeView.as_view(), name="quiz-home"),  # Your main quiz page
    path('cardset/<int:pk>/', views.CardSetPublicDetailView.as_view(), name='cardset-detail-public'),
    
]
