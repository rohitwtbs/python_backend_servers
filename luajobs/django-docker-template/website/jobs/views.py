from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.


def views():
    return HttpResponse('this is the first job opening')