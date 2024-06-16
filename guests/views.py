from django.shortcuts import render

from guests.services import get_context, get_guest


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
