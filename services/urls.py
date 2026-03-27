from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name= "register"),
    path("login", views.login_view, name= "login"),
    path("become-provider", views.become_provider, name="become_provider"),
    path("create-service", views.create_service, name="create_service"),
    path("service/<int:service_id>", views.detail, name="detail")
]