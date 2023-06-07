from django.shortcuts import render


def register(request):
    return render(request, 'users/register.html')


def login(request):
    return render(request, 'users/login.html')


def logout(request):
    return render(request, 'users/logout.html')


def profile(request):
    return render(request, 'users/profile.html')
