from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'front/index.html')

def teacher(request):
    return render(request, 'main/teacher.html')

def student(request):
    return render(request, 'front/subjects.html')

