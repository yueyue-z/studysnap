from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView
from accounts.views import login_view, register_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path("cards/", include('cards.urls', namespace='cards')),
    path('dashboard/', RedirectView.as_view(pattern_name='cards:dashboard'), name='dashboard'),
    path('login/',login_view),
    path('signup/', register_view),
    path('quiz/', include('quiz.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'), name = 'reset_password'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'), name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'), name = 'password_reset_complete'),

]
