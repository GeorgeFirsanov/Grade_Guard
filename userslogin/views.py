from django.shortcuts import render, redirect
from django.contrib import messages
from django_dump_die.middleware import dd

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
<<<<<<< HEAD
            return redirect('main\ templates\ main\student') #!!!
        else:
            #return render(request,'userlog/index.html',{'form':form})
            return redirect('signup')
    else:
        form = UserRegisterForm()
        #return render(request, 'userlog/index.html', {'form': form})
        return redirect('signup')


def signup(request):
=======
            #return render(request, 'userlog/index.html', {'form': form})
            return redirect('main\student.html') #!!! не работает
        else:
            return render(request,'userlog/index.html', {'form':form})
    else:
        form = UserRegisterForm()

        return render(request, 'userlog/index.html', {'form': form})

#синонимичный метод, только как альтернатива
def signup(request):


>>>>>>> 04716d664e804df5e053e558f1038e3ad4346235
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
<<<<<<< HEAD
            return redirect('main/templates/main/student')
=======
            return redirect('main\student.html')
>>>>>>> 04716d664e804df5e053e558f1038e3ad4346235
         
        else:
            return render(request,'userlog/index.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'userlog/index.html',{'form':form})