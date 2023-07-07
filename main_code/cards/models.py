# cards/models.py

from django.db import models

class CardSet(models.Model):
    name = models.CharField(max_length=100)

class Card(models.Model): # database model ORM
    #quiz_set = models.ForeignKey(QuizSet, on_delete=models.CASCADE, null=True, blank=True)
    card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE, related_name='cards', null=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    
