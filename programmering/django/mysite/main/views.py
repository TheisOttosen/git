from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Theis</h1> <h2>index</h2>")

def v1(response):
    return HttpResponse("<h1>Theis</h1> <h2>view 1</h2>")
