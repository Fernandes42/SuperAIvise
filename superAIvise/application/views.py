from django.shortcuts import render
from django.http import HttpResponse
from .ml import object_detect


def index(request):
    object_detect()
    return render(request, "index.html")
