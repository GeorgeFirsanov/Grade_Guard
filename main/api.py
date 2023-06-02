from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django_dump_die.middleware import dd
from group.models import Subject, Professor, Atom, Student, Category, Group
from userslogin import views as views
from main import views as mainviews

def get_professor_journal(request):
    userID = 1 #default
    if request.user.is_authenticated:
        userID = request.user.id

    #dd(Professor.objects.all())
    #dd(get_user_model())
    subjects = Professor.objects.get(user=userID).his_subject.all()
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

def get_professor_subjects_html(request):
    userID = None
    if request.user.is_authenticated:
        userID = request.user.id
    else:
        return redirect(views.signup)
    teacher = Professor.objects.get(user=userID)

    subjects = Subject.objects.filter(id = teacher.his_subject)

    sub_list = []

    for subject in subjects:
        subject_data = {"sub_name": subject.sub_name, "sub_id": subject.id}
        sub_list.append(subject_data)

    fname = request.user.first_name
    lname = request.user.last_name
    data = {"first_name": fname, "last_name": lname, "subjects": sub_list}
    return data

def get_professor_categories_html(request, subjID= None):

    if request.user.is_authenticated:
        userID = request.user.id
    else:
        return redirect(views.signup)
    teacher = Professor.objects.get(user=userID)

    if subjID == None:
        return redirect(mainviews.student)
    else:
        pass


    subject = Subject.objects.get(id=subjID)

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

    fname = request.user.first_name
    lname = request.user.last_name
    group = subject.sub_group
    data = {"first_name": fname, "last_name": lname, "group": group, "sub_name": subject.sub_name, 
            "categories": cat_list, "sub_id": subject.id}
    return data

#уже не нужен, но для пронимания общего парсинга
def get_student_journal_html(request, subjID = None):
    if request.user.is_authenticated:
        userID = request.user.id
    else:
        return redirect(views.signup)
    student = Student.objects.get(user=userID)

    subjects = None
    if subjID == None:
        subjects = Subject.objects.filter(sub_group = student.his_group)
    else: 
        subjects = Subject.objects.filter(sub_group = student.his_group).filter(id = subjID)

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

        #subject_data = {"sub_name": subject.sub_name, "categories": cat_list}
        subject_data = {"sub_name": subject.sub_name, "categories": cat_list, "sub_id": subject.id}
        sub_list.append(subject_data)

    fname = request.user.first_name
    lname = request.user.last_name
    group = student.his_group
    data = {"first_name": fname, "last_name": lname, "group": group, "subjects": sub_list}
    return data

def get_student_subjects_html(request):
    userID = None
    if request.user.is_authenticated:
        userID = request.user.id
    else:
        raise Exception("not authenticated")
    
    student = Student.objects.get(user=userID)
    #student = get_object_or_404(Student, id = userID)

    subjects = Subject.objects.filter(sub_group = student.his_group)

    sub_list = []

    for subject in subjects:
        subID = subject.id
        #subject_data = {"sub_name": subject.sub_name, "categories": cat_list}
        subject_data = {"sub_name": subject.sub_name, "sub_id": subject.id}
        sub_list.append(subject_data)

    fname = request.user.first_name
    lname = request.user.last_name
    group = student.his_group
    data = {"first_name": fname, "last_name": lname, "group": group, "subjects": sub_list}
    return data

def get_student_categories_html(request, subjID= None):

    if request.user.is_authenticated:
        userID = request.user.id
    else:
        return redirect(views.signup)
    student = Student.objects.get(user=userID)

    if subjID == None:
        return redirect(mainviews.student)
    else:
        pass


    subject = Subject.objects.get(id=subjID)

    subID = subject.id
    Categories = Category.objects.filter(subject = subID)
    cat_list = []
    total_score = 0
    for category in Categories:
        catID = category.id
        Atoms = Atom.objects.filter(category=catID) #.filter(stud_obj=userID) #ADD IT TO MAKE CORRECT QUERY!!!
        atom_list = []
        cat_total_score = 0
        for atom in Atoms:
            score = atom.scores
            cat_total_score += score
            atom_name = atom.atom_name
            atom_data = {
                "score" : score,
                "atom_name": atom_name}
            atom_list.append(atom_data)

        category_data = {"cat_name": category.cat_name, "atoms": atom_list, "score": cat_total_score}       
        cat_list.append(category_data) 
        total_score += cat_total_score

    fname = request.user.first_name
    lname = request.user.last_name
    group = student.his_group
    data = {"first_name": fname, "last_name": lname, "group": group, "sub_name": subject.sub_name, 
            "categories": cat_list, "sub_id": subject.id, "score": total_score}
    return data


def update_mark(request, atomID= None, score= None):
    if atomID == None or score == None:
        return  JsonResponse({"status": "fail"})

    Atom.objects.filter(id = atomID).update(scores = score)
    return JsonResponse({"status": "success"})


def  look_group(request):
    if request.user.is_authenticated:
        userID = request.user.id
    else:
        return redirect(views.signup)
    student = Student.objects.get(id = userID)

    group = student.his_group
    students = Student.objects.filter(his_group = group)

    stud_list = []

    for student in students:
        stud_data = {"first_name": student.user.first_name, "last_name": student.user.last_name, "user_id": student.user.id}
        stud_list.append(stud_data)

    data = {"group": group.group_name, "group_id": group, "students": stud_list}
    return data
