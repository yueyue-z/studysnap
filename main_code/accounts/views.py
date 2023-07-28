from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import forms
from django.shortcuts import render, redirect

def register_view(request):
    form = forms.CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        print(user_obj)
        return redirect('accounts:login')
    context = {"form": form}
    return render(request, "accounts/register.html", context)

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/dashboard/') # teacher login redirects to dashboard
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, "accounts/logout.html", {})