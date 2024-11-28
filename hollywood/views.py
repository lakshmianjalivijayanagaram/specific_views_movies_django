from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Titanic(request):
    return HttpResponse('<h1>Titanic is the famous hollywood movie</h1>')
def Avatar(request):
    return HttpResponse('<h1>Avatar is the top hollywood movie</h1>')