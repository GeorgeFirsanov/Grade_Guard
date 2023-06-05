from django.urls import path
from . import views, api
from userslogin import views as userv

urlpatterns = [
    path('', userv.signup, name = 'signup'),
    path('register', userv.register, name='register'),
    path('logout', userv.logout_view,  name='logout'),

    path('student', views.student, name = "student"),
    path('subject/<int:subjID>/', views.subject, name = "subject"),
    path('myGroup', views.myGroup),

    path('teacher', views.subjucts_for_prof, name = "teacher"),
    path('editTable/<int:subjID>/', views.editTable, name= "editTable"),
    

    #path('api/test', api.get_atoms)
]