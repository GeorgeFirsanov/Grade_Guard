from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django_dump_die.middleware import dd
from group.models import Subject, Professor, Atom, Student, Category, Group
from userslogin import views

def get_professor_journal(request):
    userID = 1 #default
    if request.user.is_authenticated:
        userID = request.user.id

    #dd(Professor.objects.all())
    #dd(get_user_model())
    subjects = Professor.objects.get(id=userID).his_subject.all()
    responseJson = {}
    response = []
    for subject in subjects:
        subID = subject.id
        #Atoms = Atom.objects.get(subject_id=subID)
        Atoms = Atom.objects.filter(subject_id=subID)
        for atom in Atoms:
        #atom = Atom.objects.get(subject_id=subID)
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
            #Professor
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

def get_student_journal(request):

    userID = 1 #default
    if request.user.is_authenticated:
        userID = request.user.id
    student = Student.objects.get(id=userID)
    subjects = Subject.objects.filter(sub_group = student.his_group)

    #subjects = Subject.objects.all()
    responseJson = {}
    response = []
    for subject in subjects:
        subID = subject.id
        #Atoms = Atom.objects.get(subject_id=subID)
        Atoms = Atom.objects.filter(subject_id=subID)
        for atom in Atoms:
        #atom = Atom.objects.get(subject_id=subID)
            score = atom.scores
            teacher = Professor.objects.get(id = atom.stud_obj_id)
            user = User.objects.get(id = teacher.user_id)
            lastName = user.last_name
            firstName = user.first_name
            #group = Group.objects.get(id = teacher.his_group_id)
            #groupName = group.group_name
            category = Category.objects.get(id = atom.category_id)
            categoryName = category.cat_name
            subName = subject.sub_name
            #Professor
            json = {
                "lastName" : lastName,
                "firstName" : firstName,
                "category" : categoryName,
                "score" : score,
                "subjectName" : subName,
            }
            response.append(json)
    responseJson["marks"] = response
    ##dd(response)
    return JsonResponse(responseJson)

def get_student_journal_html(request):

    userID = 1 #default
    if request.user.is_authenticated:
        userID = request.user.id
    student = Student.objects.get(id=userID)
    subjects = Subject.objects.filter(sub_group = student.his_group)

    #subjects = Subject.objects.all()
    sub_list = []

    for subject in subjects:
        subID = subject.id
        Categories = Category.objects.filter(subject = subID)
        cat_list = []

        for category in Categories:
            catID = category.id
            Atoms = Atom.objects.filter(category=catID) #.filter(stud_obj=userID) #ADD IT TO MAKE CORRECT QUERY!!!
            atom_list = []

            for atom in Atoms:
                score = atom.scores
                atom_name = atom.atom_name
                atom_data = {
                    "score" : score,
                    "atom_name": atom_name}
                atom_list.append(atom_data)

            category_data = {"cat_name": category.cat_name, "atoms": atom_list}       
            cat_list.append(category_data) 

        subject_data = {"sub_name": subject.sub_name, "categories": cat_list}
        sub_list.append(subject_data)

    fname = request.user.first_name
    lname = request.user.last_name
    group = student.his_group
    data = {"first_name": fname, "last_name": lname, "group": group, "subjects": sub_list}
    return data

def update_mark(request):
    atomId = 1
    score = 1
    Atom.objects.filter(id = atomId).update(scores = score)
    return JsonResponse({"status": "success"})

