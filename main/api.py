from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django_dump_die.middleware import dd
from group.models import Subject, Professor, Atom, Student, Category, Group
from userslogin import views

def get_professor_journal(request):
    #dd(Professor.objects.all())
    #dd(get_user_model())
    subjects = Professor.objects.get(id=1).his_subject.all()
    responseJson = {}
    response = []
    for subject in subjects:
        subID = subject.id
        atom = Atom.objects.get(subject_id=subID)
        score = atom.scores
        student = Student.objects.get(id = atom.stud_obj_id)
        user = User.objects.get(id = student.user_id)
        lastName = user.last_name
        firstName = user.first_name
        group = Group.objects.get(id = student.his_group_id)
        groupName = group.group_name
        category = Category.objects.get(id = atom.category_id)
        categoryName = category.cat_name
        subName = subject.sub_name
        Professor
        json = {
            "lastName" : lastName,
            "firstName" : firstName,
            "category" : categoryName,
            "score" : score,
            "subjectName" : subName,
            "groupName" : groupName,

        }
        response.append(json)
    responseJson["marks"] = response
    ##dd(response)
    return JsonResponse(responseJson)


def update_mark(request):
    atomId = 1
    score = 1
    Atom.objects.filter(id = atomId).update(scores = score)
    return JsonResponse({"status": "success"})



