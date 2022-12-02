from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(
        "<html>"
        "<h1>task manager</h1>"
        "</html>"

    )
