from django.shortcuts import render, redirect
from reserv.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {
        'page': 'home',
    }
    return render(
        request,
        'reserv/index.html',
        context
    )


def eventos(request):
    context = {
        'page': 'eventos',
    }
    return render(
        request,
        'reserv/eventos.html',
        context
    )


def reserva(request):
    context = {
        'page': 'reservas',
    }
    return render(
        request,
        'reserv/reserva.html',
        context
    )


def login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('reserv:index')

    context = {
        'page': 'login',
        'form': form
    }
    return render(
        request,
        'reserv/login.html',
        context
    )


def register_login(request):
    form = RegisterForm()
    context = {
        'form': form,
        'page': 'register',
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reserv:login')

    return render(
        request,
        'reserv/register.html',
        context
    )


@login_required(login_url='reserv:login')
def logout(request):
    auth.logout(request)
    return redirect('reserv:login')
