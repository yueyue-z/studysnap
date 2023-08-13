from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# register, login and logout views

def register_view(request):
    form = forms.CustomUserCreationForm(request.POST or None)
    
    if form.is_valid():
        user_obj = form.save(commit=False)  # Don't save yet, so we can perform additional checks
        existing_user = User.objects.filter(email=user_obj.email).first()
        
        if existing_user:
            messages.error(request, "This email already exists. Please login or reset password.")
        else:
            user_obj.save()
            return redirect('accounts:login')
    
    context = {"form": form}
    return render(request, "accounts/register.html", context)


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