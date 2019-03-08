from django.contrib import admin

from .models import Donation, Subscription

# Register your models here.

admin.site.register(Donation, admin.ModelAdmin)
admin.site.register(Subscription, admin.ModelAdmin)
