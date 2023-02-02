from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, world. are You fine?")

# Create your views here.
