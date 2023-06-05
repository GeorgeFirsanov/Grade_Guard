from django.shortcuts import render, redirect
from django.http import HttpResponse
from group.models import Subject
from main.api import get_student_subjects_html, get_student_categories_html, look_group, get_professor_subjects, tempo_dataset
from userslogin import views

def teacher(request):
    if request.user.is_authenticated:
        return render(request, 'front/gropus.html')
    else:
        return redirect(views.signup)

def student(request):
    #'or True' is temporary solution
    if request.user.is_authenticated:
        data = None
        try:
            data = get_student_subjects_html(request)
        except Exception:
            redirect(views.signup)
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

def myGroup(request):
    if request.user.is_authenticated:
            data = look_group(request)
            return render(request, 'front/myGroup.html', data)
    else:
        return redirect(views.signup)

def subjucts_for_prof(request):
    if request.user.is_authenticated:
            data = get_professor_subjects(request)
            return render(request, 'front/subjects_prof.html', data)
    else:
        return redirect(views.signup)

def editTable(request, subjID):
    #'or True' is temporary solution
    if request.user.is_authenticated:
            data = tempo_dataset()
            return render(request, 'front/editTable.html', data)
    else:
        return redirect(views.signup)