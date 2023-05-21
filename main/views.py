from django.shortcuts import render, redirect
from django.http import HttpResponse
from group.models import Subject
from userslogin import views

def teacher(request):
    
    if request.user.is_authenticated:
        return render(request, 'main/teacher.html')
    else:
        return redirect(views.register)

def student(request):
    #'or True' is temporary solution
    if request.user.is_authenticated or True:
        return render(request, 'front/subjects.html')
    else:
        return redirect(views.register)

def subject(request):
    if request.user.is_authenticated or True:
            return render(request, 'front/marks.html', {'subjects': Subject.objects.all()})
    else:
        return redirect(views.register)

