from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('teacher', views.teacher),
    path('student', views.student),
    path('subject', views.subject),
    path("register", views.register_request, name="register")
]