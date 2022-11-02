from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Marat!")
# Create your views here.
