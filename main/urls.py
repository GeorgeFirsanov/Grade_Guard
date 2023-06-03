from django.urls import path
from . import views, api
from userslogin import views as userv

urlpatterns = [
    path('', userv.signup, name = 'signup'),
    path('register', userv.register, name='register'),
    path('logout', userv.logout_view,  name='logout'),

    path('teacher', views.teacher),
    path('student', views.student, name = "student"),
    path('subject/<int:subjID>/', views.subject, name = "subject"),
    path('myGroup', views.myGroup),

    path('api/get_journal', api.get_professor_journal),
    path('api/mymarks/<int:subjID>/', api.get_student_journal_html, name = 'api/mymarks'),
    path('api/updatemark', api.update_mark),

    path('test', api.look_group)
]