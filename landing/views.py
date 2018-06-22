from django.shortcuts import render


def land(request):
    return render(request, 'base.html')
