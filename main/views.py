from django.shortcuts import render, redirect
from django.http import HttpResponse
from group.models import Subject
from main.api import get_student_subjects_html, get_student_categories_html
from userslogin import views

def teacher(request):
    
    if request.user.is_authenticated:
        return render(request, 'front/gropus.html')
    else:
        return redirect(views.signup)

def student(request):
    #'or True' is temporary solution
    if request.user.is_authenticated:
        data = get_student_subjects_html(request)
        return render(request, 'front/subjects.html', data)
    else:
        return redirect(views.signup)

def subject(request, subjID):
    #'or True' is temporary solution
    if request.user.is_authenticated:
            data = get_student_categories_html(request, subjID)
            return render(request, 'front/marks.html', data)
    else:
        return redirect(views.signup)

