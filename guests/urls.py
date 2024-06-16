from django.urls import path
from . import views as v


urlpatterns = [
    path('<slug:slug>', v.invitation, name="Страница приглашения")
]
