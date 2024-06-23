from django.contrib import admin
from django.utils.html import format_html

from . import models as m


@admin.register(m.GuestModel)
class GuestModelAdmin(admin.ModelAdmin):
    list_display = 'name', 'view_link',
    readonly_fields = ('view_link', 'date_time_answer', )

    def get_fieldsets(self, request, obj=None):
        if obj is None or obj.pk is None:
            fieldsets = (
                (None, {
                    'fields': ('name', 'name_guest',)
                }),
            )
        elif obj.visit:
            if obj.visit == 'да':
                fieldsets = (
                    (None, {
                        'fields': ('name', 'name_guest', 'view_link', 'visit', 'drinks', 'date_time_answer', )
                    }),
                )
            else:
                fieldsets = (
                    (None, {
                        'fields': ('name', 'name_guest', 'view_link', 'visit', 'date_time_answer', )
                    }),
                )
        else:
            fieldsets = (
                (None, {
                    'fields': ('name', 'name_guest', 'view_link', )
                }),
            )

        return fieldsets

    def view_link(self, obj):
        # Возвращает HTML-код ссылки
        return format_html("<a href='{url}'>Просмотр</a>", url=obj.get_absolute_url())
    view_link.short_description = "Ссылка на статью"


# @admin.register(m.CityModel)
# class CityModelAdmin(admin.ModelAdmin):
#     pass


@admin.register(m.DrinkModel)
class DrinkModelAdmin(admin.ModelAdmin):
    pass


@admin.register(m.EventModel)
class EventModelAdmin(admin.ModelAdmin):
    pass
