from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def playing(request):
    return HttpResponse('nikky is palying cricket')


