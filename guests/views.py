from django.shortcuts import render


def invitation(request):
    method = request.method

    # if method == "GET":
    return render(request, 'invitation.html')
    # return render(request, 'index.html')
