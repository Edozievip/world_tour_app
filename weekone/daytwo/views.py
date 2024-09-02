from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is my day two in 3mtt practical class @ <em>Awka</b>.</h1>")