from django.shortcuts import render
from django.http import HttpResponse

from group.models import Subject

def register_request(request):
    return render(request, 'front/index.html')

def teacher(request):
    return render(request, 'main/teacher.html')

def student(request):
    return render(request, 'front/subjects.html')

def subject(request):
    return render(request, 'front/marks.html', {'subjects': Subject.objects.all()})

