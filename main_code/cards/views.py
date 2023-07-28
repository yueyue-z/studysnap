# cards/views.py
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Card, CardSet
from .forms import CardSetForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

@login_required
def CardSetCreateView(request):
    submitted = False
    if request.method == 'POST':
        form = CardSetForm(request.POST)

        if request.user.is_authenticated:
            author = User.objects.get(pk=request.user.id)
            form.instance.author = author
           

        if form.is_valid():
            form.save()
            return HttpResponseRedirect ('/cards/cardset?submitted=True')
        
    else:
        form = CardSetForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'cards/cardset_form.html',{'form':form, 'submitted': submitted})


class CardSetListView(LoginRequiredMixin, ListView):
    model = CardSet
    queryset = CardSet.objects.all()
    template_name = 'cards/cardset_list.html'  # Path to your CardSet list template
    context_object_name = 'cardsets'  # Name of the variable to be used in the template

# class CardSetCreateView(LoginRequiredMixin, CreateView):
#     model = CardSet
#     fields = ["name", "description"]
#     success_url = reverse_lazy("cards:cardset-list")

class CardSetUpdateView(LoginRequiredMixin, UpdateView):
    model = CardSet
    fields = ["name"]
    success_url = reverse_lazy("cards:cardset-list")

class CardSetDeleteView(LoginRequiredMixin, DeleteView):
    model = CardSet
    success_url = reverse_lazy('cards:cardset-list')

class CardSetDetailView(LoginRequiredMixin, DetailView):
    model = CardSet
    template_name = 'cards/cardset_detail.html'  # Path to your CardSet detail template
    context_object_name = 'cardset'  # Name of the variable to be used in the template
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cardset = self.get_object()
        context['cards'] = cardset.card_set.all()
        return context

class CardListView(LoginRequiredMixin, ListView):
    model = Card
    queryset = Card.objects.all()

class CardCreateView(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    redirect_field_name = "redirected_to"
    model = Card
    fields = ["question", "answer"]  # remove card_set from here

    def form_valid(self, form):
        form.instance.card_set = get_object_or_404(CardSet, id=self.kwargs['cardset_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("cards:cardset-detail", kwargs={'pk': self.kwargs['cardset_id']})

class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ["question", "answer", "card_set"]
    success_url = reverse_lazy("cards:dashboard")

class DashboardView(LoginRequiredMixin, ListView):
    model = CardSet  # Changed from Card to CardSet
    template_name = 'cards/dashboard.html'
    context_object_name = 'cardsets'  # Changed from 'cards' to 'cardsets'

    def get_queryset(self):
        # Filter the CardSet model by the current user
        return CardSet.objects.filter(author_id=self.request.user.id)




class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = reverse_lazy('cards:dashboard')

def card_question_view(request, pk):
    card = Card.objects.get(id=pk)
    return render(request, 'question_card.html', {'card': card})
