from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")