from django.contrib import admin
from rest_framework.authtoken.models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
