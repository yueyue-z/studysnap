from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView
from accounts.views import login_view, register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path("cards/", include('cards.urls', namespace='cards')),
    path('dashboard/', RedirectView.as_view(pattern_name='cards:dashboard'), name='dashboard'),
    path('login/',login_view),
    path('signup/', register_view),
    path('quiz/', include('quiz.urls')),

]
