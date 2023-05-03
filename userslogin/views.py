from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register1(request):
    return render(request, 'userlog/index.html')

def register(request):
    if request.method == 'POST':
        print("post")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('student')
    else:
        form = UserRegisterForm()
    return render(request, 'userlog/index.html', {'form': form})