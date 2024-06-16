from django.contrib import admin
from django.utils.html import format_html

from . import models as m


@admin.register(m.GuestModel)
class GuestModelAdmin(admin.ModelAdmin):
    list_display = 'name', 'view_link',

    # def get_fieldsets(self, request, obj=None):
    #     if obj and obj.visit:
    #         ...

    def view_link(self, obj):
        # Возвращает HTML-код ссылки
        return format_html("<a href='{url}'>Просмотр</a>", url=obj.get_absolute_url())
    view_link.short_description = "Ссылка на статью"


@admin.register(m.CityModel)
class CityModelAdmin(admin.ModelAdmin):
    pass


@admin.register(m.DrinkModel)
class DrinkModelAdmin(admin.ModelAdmin):
    pass


@admin.register(m.EventModel)
class EventModelAdmin(admin.ModelAdmin):
    pass
