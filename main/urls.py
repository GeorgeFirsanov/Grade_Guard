from django.urls import path
from . import views, api
from userslogin import views as userv

urlpatterns = [
    path('', userv.signup, name = 'signup'),
    path('register', userv.register, name = 'register'),
    path('teacher', views.teacher),
    path('student', views.student),
<<<<<<< HEAD
    path('subject', views.subject)
=======
    path('subject', views.subject),
    path('api/get_journal', api.get_professor_journal),
    path('api/updatemark', api.update_mark),
>>>>>>> 04716d664e804df5e053e558f1038e3ad4346235
]