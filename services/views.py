from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from .models import User, Service, ProviderProfile, Booking

# Create your views here.


def index(request):
    return render(request, "services/index.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get["username"]
        password = request.POST.get["password"]
        email = request.POST.get["email"]
        confirmation = request.POST.get["confirm"]

        if not username or not email or not password or not confirmation:
            return render(request, "services/register.html", {
                "message": "All fields are required"
            })
        if confirmation != password:
            return render(request, "services/register.html", {
                "message": "Password must match"
            })
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, "services/register.html", {
                "message": "username is taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "services/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
        else:
            return render(request, "services/login.html", {
                "message":"user does not exist"
            })
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "services/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
