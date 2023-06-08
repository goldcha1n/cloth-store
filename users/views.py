from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import *


def register(request):
    return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # Получает данные из формы и записывает их как HTML формат, данный содержаться в value.
        if form.is_valid():  # Проверяет эту html форму на валидность, если она валидна выполняются следующие действия
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # Поиск в БД пользователя с таким паролем и логином
            if user:  # Если такой пользователь существует
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
    else:  # Если это GET запрос
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


# def logout(request):
#     return render(request, 'users/logout.html')


def profile(request):
    return render(request, 'users/profile.html')
