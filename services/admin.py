from django.contrib import admin

from .models import User, Service, ProviderProfile, Booking
# Register your models here.

admin.site.register(User)
admin.site.register(Service)
admin.site.register(ProviderProfile)
admin.site.register(Booking)