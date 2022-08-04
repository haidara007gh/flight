from django.contrib import admin
from flights.models import *

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")
# Register your models here.
admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger)