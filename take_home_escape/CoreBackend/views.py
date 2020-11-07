from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def AboutUs(request):
    Data = {}
    return render(request, "CoreBackend/index.html", Data)


def ManualPage(request):
    Data = {}
    return render(request, "CoreBackend/manual.html", Data)
