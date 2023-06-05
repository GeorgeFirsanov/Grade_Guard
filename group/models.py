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

<<<<<<< HEAD
    def __str__(self):
        return (
            f"{self.group_name} "
        )

=======
>>>>>>> c05ce29b28c2fc84802b8cf8931a9d892b8fe274

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    his_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

<<<<<<< HEAD
    def __str__(self):
        return (
            f"{self.user} "
            f"{self.user.first_name} "
            f"{self.user.last_name} "
        )

=======
>>>>>>> c05ce29b28c2fc84802b8cf8931a9d892b8fe274

class Subject(models.Model):
    sub_name = models.CharField(max_length=32)
    sub_group = models.ForeignKey(Group, on_delete=models.CASCADE)

<<<<<<< HEAD
    def __str__(self):
        return (
            f"{self.sub_group} "
            f"{self.sub_name} "
        )

=======
>>>>>>> c05ce29b28c2fc84802b8cf8931a9d892b8fe274

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    his_subject = models.ManyToManyField(Subject)

<<<<<<< HEAD
    def __str__(self):
        return (
            f"{self.user} "
            f"{self.user.first_name} "
            f"{self.user.last_name} "
        )

=======
>>>>>>> c05ce29b28c2fc84802b8cf8931a9d892b8fe274

class Category(models.Model):
    cat_name = models.CharField(max_length=32)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
<<<<<<< HEAD
=======

>>>>>>> c05ce29b28c2fc84802b8cf8931a9d892b8fe274

    def __str__(self):
        return (
            f"{self.subject} "
            f"{self.cat_name} "
        )
    
class Atom(models.Model):
    stud_obj = models.ForeignKey(Student, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
<<<<<<< HEAD
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null = True)
    atom_name = models.CharField(max_length=16, null = True)

    def __str__(self):
        return (
            f"{self.scores} "
            f"{self.stud_obj.user.first_name} "
            f"{self.stud_obj.user.last_name} "
            f"{self.subject} "
        )
=======
>>>>>>> c05ce29b28c2fc84802b8cf8931a9d892b8fe274
