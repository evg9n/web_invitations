from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.main_page, name="Страница приглашения"),
    path('<slug:slug>', v.invitation, name="Страница приглашения"),
]
