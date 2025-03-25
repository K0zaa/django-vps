from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Ahoj, tohle je můj první Django projekt!")
