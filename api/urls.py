from django.urls import path

from guests.views import generate_file_result

urlpatterns = [
    path('get-result', generate_file_result, name='Выгрузка результатов')
]
