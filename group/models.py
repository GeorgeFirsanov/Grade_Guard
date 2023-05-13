from django.db import models
from django.contrib.auth.models import User

''' 
    --SUDENT--  --one_to_one---> --USER--
        |  one    
       \|/ to many   

    --GROUP--

       /|\ to many
        |  one         many to many
    --SUBJECT--       <------------ --PROFESSOR--

       /|\ to many
        |  one
    --CATEGORY--

       /|\ to many
        |  one
    --ATOM--   
        |  one
       \|/ to many
    --STUDENT--
'''


class Group(models.Model):
    group_name = models.CharField(max_length=16, null='')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    his_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


class Subject(models.Model):
    sub_name = models.CharField(max_length=32)
    sub_group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    his_subject = models.ManyToManyField(Subject)


class Category(models.Model):
    cat_name = models.CharField(max_length=32)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Atom(models.Model):
    #имя атома
    stud_obj = models.ForeignKey(Student, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
