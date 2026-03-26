from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name= "register"),
    path("login", views.login_view, name= "login"),
    path("become-provider", views.become_provider, name="become_provider"),
]