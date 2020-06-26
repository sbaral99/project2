from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#creating function based views
#request will b in the form of http
#so we hv to respond back for the request in the form of http only

def Read(request):
    return HttpResponse('<h1><marquee>ashu is reading a novel</marquee></h1>')
def Write(request):
    return HttpResponse('ashu is writting')