from django.urls import path
from . import views

# url for homepage

app_name = 'home'

urlpatterns = [
    path('', views.homepage, name='home'),
]