from django.contrib import admin
from . import models as m


@admin.register(m.GuestModel)
class GuestModelAdmin(admin.ModelAdmin):
    pass


@admin.register(m.CityModel)
class CityModelAdmin(admin.ModelAdmin):
    pass


@admin.register(m.DrinkModel)
class DrinkModelAdmin(admin.ModelAdmin):
    pass
