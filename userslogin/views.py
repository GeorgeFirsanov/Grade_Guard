from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm


def register(request):
    form = NewUserForm(request)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Создан аккаунт {username}!')
        return redirect('blog-home')
    return render(request, 'users/register.html', {'form': form})
