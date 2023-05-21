from django.urls import path
from . import views, api
from userslogin import views as userv

urlpatterns = [
    path('', userv.signup, name = 'signup'),
    path('register', userv.register, name='register'),
    path('logout', userv.logout_view,  name='logout'),

    path('teacher', views.teacher),
    path('student', views.student),
    path('subject', views.subject),

    path('api/get_journal', api.get_professor_journal),
    path('api/mymarks', api.get_student_journal),
    path('api/updatemark', api.update_mark),
]