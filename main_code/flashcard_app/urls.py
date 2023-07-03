from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from cards.views import CardListView
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cards/', include('cards.urls', namespace='cards')),  # all card URLs are prefixed with 'cards/'
    path('', CardListView.as_view(), name='home'),  # home page URL is the CardListView
    path('dashboard/', RedirectView.as_view(pattern_name='cards:dashboard'), name='dashboard'),
    # more paths as necessary
]
