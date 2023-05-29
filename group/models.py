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

    def __str__(self):
        return (
            f"{self.group_name} "
        )


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    his_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"{self.user.first_name} "
            f"{self.user.last_name} "
        )


class Subject(models.Model):
    sub_name = models.CharField(max_length=32)
    sub_group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"{self.sub_group} "
            f"{self.sub_name} "
        )


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    his_subject = models.ManyToManyField(Subject)

    def __str__(self):
        return (
            f"{self.user} "
            f"{self.user.first_name} "
            f"{self.user.last_name} "
        )


class Category(models.Model):
    cat_name = models.CharField(max_length=32)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"{self.subject} "
            f"{self.cat_name} "
        )
    
class Atom(models.Model):
    stud_obj = models.ForeignKey(Student, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null = True)
    atom_name = models.CharField(max_length=16, null = True)

    def __str__(self):
        return (
            f"{self.scores} "
            f"{self.stud_obj.user.first_name} "
            f"{self.stud_obj.user.last_name} "
            f"{self.subject} "
        )
