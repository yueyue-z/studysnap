# cards/urls.py

from django.urls import path
# Removed: from django.views.generic import TemplateView

from . import views

urlpatterns = [

    path(
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
    ),

    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),

    path(
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name = 'box'
    ),
]