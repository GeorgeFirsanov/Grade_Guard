from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('main\ templates\ main\student') #!!!
        else:
            #return render(request,'userlog/index.html',{'form':form})
            return redirect('signup')
    else:
        form = UserRegisterForm()
        #return render(request, 'userlog/index.html', {'form': form})
        return redirect('signup')


def signup(request):
    if request.user.is_authenticated:
        #return redirect ('student')
        pass
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request= request, user= user)
            return redirect('main/templates/main/student')
         
        else:
            return render(request,'userlog/index.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'userlog/index.html',{'form':form})