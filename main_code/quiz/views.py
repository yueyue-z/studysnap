# quiz/views.py

from django.shortcuts import render
from django.views import View
from cards.models import CardSet
from django.views.generic import  DetailView
from django.db.models import Count

class QuizHomeView(View):
    def get(self, request):
        query = request.GET.get('q')

        if query is not None:
            cardsets = CardSet.objects.annotate(num_cards=Count('card')).filter(name__icontains=query, num_cards__gt=0)
        else:
            cardsets = CardSet.objects.annotate(num_cards=Count('card')).filter(num_cards__gt=0)

        return render(request, 'quiz/home.html', {'cardsets': cardsets})

class CardSetPublicDetailView(DetailView):
    model = CardSet
    template_name = 'quiz/quiz_details.html'  # Path to your public CardSet detail template
    context_object_name = 'cardset'  # Name of the variable to be used in the template
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cardset = self.get_object()
        context['cards'] = cardset.card_set.all()
        return context  