from django.shortcuts import render, redirect
from django.contrib import messages
from django_dump_die.middleware import dd

from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login, logout


def signup(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password = password)
            login(request= request, user= user)
            if hasattr(user, 'professor'):
                return redirect('/teacher')
            else:
                return redirect('/student')
        else:
            return render(request,'userlog/index.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'userlog/index.html',{'form':form})
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

