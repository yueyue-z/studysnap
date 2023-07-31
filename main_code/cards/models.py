# cards/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

User = settings.AUTH_USER_MODEL

class CardSet(models.Model):
    author = models.ForeignKey(User, blank = True, null = True, on_delete=models.SET_NULL)
    name = models.TextField() 
    description = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)



class Card(models.Model): # database model ORM
    question = models.TextField()
    answer = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    card_set = models.ForeignKey(CardSet, on_delete = models.CASCADE, null=True,blank = True)
    
