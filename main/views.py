from django.shortcuts import render, redirect
from django.http import HttpResponse
from group.models import Subject
from main.api import get_student_journal_html
from userslogin import views

def teacher(request):
    
    if request.user.is_authenticated:
        return render(request, 'front/gropus.html')
    else:
        return redirect(views.signup)

def student(request, subject_ID):
    #'or True' is temporary solution
    if request.user.is_authenticated:
        data = get_student_journal_html(request, subjID=subject_ID)
        return render(request, 'front/subjects.html', data)
    else:
        return redirect(views.signup)

def subject(request):
    #'or True' is temporary solution
    if request.user.is_authenticated or True:
            return render(request, 'front/marks.html', {'subjects': Subject.objects.all()})
    else:
        return redirect(views.signup)

