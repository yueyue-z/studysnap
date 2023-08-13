from django.urls import path
from . import views

# urls for login, logout and register

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("register/", views.register_view, name='register'),
]
