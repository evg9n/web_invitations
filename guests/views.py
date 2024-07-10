from io import BytesIO

from django.shortcuts import render
from django.http import HttpResponseNotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
from xlsxwriter import Workbook

from guests.services import get_context, get_guest, answers_guest, generate_excel


def main_page(request):
    if request.method == 'GET':
        context = get_context()
        return render(request=request, template_name='main.html', context=context)


def invitation(request, **kwargs):
    method = request.method
    slug = kwargs.get('slug')

    if method == 'GET':
        if slug:
            guest = get_guest(slug=slug)
            if guest:
                context = get_context()
                context['guest'] = guest
                return render(request=request, template_name='invitation.html', context=context)
        else:
            return HttpResponseNotFound('What do you want from me?')

    elif method == 'POST':
        if slug:
            request_post = request.POST
            guest = get_guest(slug=slug)
            if guest and answers_guest(guest=guest, request_post=request_post):
                guest = get_guest(slug=slug)
                context = get_context()
                context['guest'] = guest
                context['message'] = 'Будем Вас ждать!' if guest.visit == 'да' else 'Жаль что Вы не придете'
                return render(request=request, template_name='invitation.html', context=context)

    return HttpResponseNotFound('What do you want from me?')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_file_result(request):
    if request.method == "GET":
        output = generate_excel(request)
        # Отправляем файл в ответе
        response = HttpResponse(output.read(),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="example.xlsx"'
        return response
