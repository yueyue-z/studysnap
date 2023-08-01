from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
\
    path("new/", views.CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("view-question/<int:pk>",views.card_question_view,name="card-question"),
    path("dashboard/",views.DashboardView.as_view(),name="dashboard"),
    path('delete/<int:pk>', views.CardDeleteView.as_view(), name='card-delete'),
    path("", views.CardListView.as_view()),
    # Add these paths for the CardSet views
    path("cardset/new/", views.CardSetCreateView, name="cardset-create"),
    path("cardset/edit/<int:pk>", views.CardSetUpdateView.as_view(), name="cardset-update"),
    path("cardset/<int:pk>", views.CardSetDetailView.as_view(), name="cardset-detail"),
    path("cardset/delete/<int:pk>", views.CardSetDeleteView.as_view(), name="cardset-delete"),
    path("cardset/<int:cardset_id>/new/", views.CardCreateView.as_view(), name="card-create"),

]
