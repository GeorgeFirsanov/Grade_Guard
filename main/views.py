from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3>Main</h3>")

def teacher(request):
    return HttpResponse("<h3>teacher</h3>")
# Create your views here.
