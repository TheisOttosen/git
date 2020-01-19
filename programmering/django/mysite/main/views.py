from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    items = ls.item_set.all()
    return HttpResponse("<h1>%s</h1><br></br><h2>%s</h2>" %(ls.name, items.get(id=1)))

