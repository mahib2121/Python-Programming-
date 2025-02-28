from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")


def Mb(request):
    return HttpResponse("<h1>Hello</h1>")


def mahib(request):
    return render(request, "first.html")
