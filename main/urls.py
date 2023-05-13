from django.urls import path
from . import views
from userslogin import views as userv

urlpatterns = [
    path('', userv.signup, name = 'signup'),
    path('register', userv.register, name = 'register'),
    path('teacher', views.teacher),
    path('student', views.student),
    path('subject', views.subject)
]