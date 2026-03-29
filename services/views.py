from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import User, Service, ProviderProfile, Booking

# Create your views here.


def index(request):
    services = Service.objects.all()
    return render(request, "services/index.html", {
        "services": services
    })

@login_required
def dashboard(request, username):
    user = User.objects.get(username=username)
    provider = ProviderProfile.objects.filter(user=request.user).first()
    services = Service.objects.filter(provider = provider)
    bookings = None
    if provider:
        bookings = Booking.objects.filter(provider= provider)
    else:
        bookings = Booking.objects.filter(user=request.user)
    return render(request, "services/dashboard.html", {
        "user": user,
        "provider": provider,
        "services": services,
        "bookings": bookings,
    })


@login_required
def book_service(request, service_id):
    service = Service.objects.get(id=service_id)

    if Booking.objects.filter(user=request.user, service=service).exists():
        messages.error(request, "Already booked")
        return redirect("dashboard", username= request.user.username)

    booking = Booking.objects.create(
        user= request.user,
        provider = service.provider,
        service = service,
    )
    booking.save()

    return redirect("dashboard", username= request.user.username)


@login_required
def delete_service(request, service_id):
    service = Service.objects.get(id=service_id)

    if service.provider.user != request.user:
        return redirect("dashboard", username= request.user.username)
    
    if request.method == "POST":
        service.delete()   

    return redirect("dashboard", username= request.user.username)


@login_required
def edit_service(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.user == service.provider.user:
        if request.method == "POST":
            print(request.POST)
            name = request.POST.get("name")
            description = request.POST.get("description")
            price = request.POST.get("price")
            service.name = name
            service.description = description
            service.price = price
            service.save()
            return redirect("detail", service_id= service_id)
        return render(request, "services/create_service.html", {
            "service": service
        })
    else:
        return redirect("dashboard", username=request.user.username)


@login_required
def status_update(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    
    if request.user != booking.provider.user:
        return redirect("dashboard", username= request.user.username)
    
    if request.method == "POST":
        booking = Booking.objects.get(id=booking_id)
        if 'accept' in request.POST:
            booking.status = "accepted"
            booking.save()
        elif 'reject' in request.POST:
            booking.status = "rejected"
            booking.save()    
    
    return redirect("dashboard", username= request.user.username)


@login_required
def detail(request, service_id):
    service = Service.objects.get(id = service_id)
    bookings = Booking.objects.filter(service = service)
    already_booked = False 
    for booking in bookings:
        if booking.user == request.user:
            already_booked = True
    return render(request, "services/detail.html", {
        "service": service,
        "already_booked": already_booked,
    })

@login_required
def become_provider(request):
    if request.method == "POST":
        description = request.POST.get("description")

        if ProviderProfile.objects.filter(user = request.user).exists():
            return render(request, "services/become_provider.html", {
                "message": "Provider profile already exists"
            })
        provider = ProviderProfile.objects.create(user = request.user, description = description)
        provider.save()
        messages.success(request, "You are a provider now !!")
        return HttpResponseRedirect(reverse("index"))
    user = User.objects.get(username = request.user.username)
    return render(request, "services/become_provider.html", {
        "user": user
    })


@login_required
def create_service(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        provider = ProviderProfile.objects.get(user = request.user)
        if not name or not description or not price:
            return render(request, "services/create_service.html", {
                "message": "All fields are required"
            })
        if not provider:
                messages.error(request, "You are not a provider")
                return HttpResponseRedirect(reverse("index"))
        service = Service.objects.create(name = name, description = description, price = price, provider = provider)
        service.save()
        messages.success(request, "Service created successfully")
        return HttpResponseRedirect(reverse("index"))
    return render(request, "services/create_service.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        confirmation = request.POST.get("confirm")

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
        messages.success(request, "Account created successfully")
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
