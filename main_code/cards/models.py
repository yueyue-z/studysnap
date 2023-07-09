# cards/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CardSet(models.Model):
    name = models.CharField(max_length=100) # for large amounts of text, yuse TextField
    date_created = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if the user is deleted, so is the quiz set

class Card(models.Model): # database model ORM
    #quiz_set = models.ForeignKey(QuizSet, on_delete=models.CASCADE, null=True, blank=True)
    card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE, related_name='cards', null=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    
