from django.shortcuts import render
from django.http import HttpResponseNotFound

from guests.services import get_context, get_guest, answers_guest


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
                return render(request=request, template_name='invitation.html', context=context)

    return HttpResponseNotFound('What do you want from me?')
