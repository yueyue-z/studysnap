# cards/views.py
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CardCheckForm
from .models import Card # add QuizSet

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all()

class CardCreateView(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    redirect_field_name = "redirected_to"
     # doesnt matter cause we have a dashboard redirect in accounts
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("cards:home")

class CardUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/accounts/login/"
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-list")


class BoxView(CardListView):
    template_name = 'cards/box.html'
    form_class = CardCheckForm

class DashboardView(LoginRequiredMixin, ListView):
    login_url = "/accounts/login/"
    redirect_field_name = "redirected_to"
    model = Card
    template_name = 'cards/dashboard.html'  # Set the correct path to your template
    context_object_name = 'cards'  # Name of the variable to be used in the template

class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = reverse_lazy('cards:dashboard')


    def get_queryset(self):
      return Card.objects.filter(box=self.kwargs["box_num"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_number'] = self.kwargs['box_num']
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))
    

def card_question_view(request, pk):
    card = Card.objects.get(id=pk)
    return render(request, 'question_card.html', {'card': card})
