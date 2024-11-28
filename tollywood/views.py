from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def bahubali(request):
    return HttpResponse('<h1>Bahubali is the famous panindia Movie</h1>')
def RRR(request):
    return HttpResponse('<h1>RRR is the TFI standard Movie</h1>')