from django.contrib import admin
from flights.models import *

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger)