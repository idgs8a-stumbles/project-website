# example/views.py
from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    return render(request,'example/index.html', {"current_time":now})


def not_found(request):
    return render(request, '404.html')

def blank(request):
    return render(request, 'blank.html')

def buttons(request):
    return render(request, 'buttons.html')

def cards(request):
    return render(request, 'cards.html')

def charts(request):
    return render(request, 'charts.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

def user_login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def tables(request):
    return render(request, 'tables.html')

def utilities_animation(request):
    return render(request, 'utilities-animation.html')

def utilities_border(request):
    return render(request, 'utilities-border.html')

def utilities_color(request):
    return render(request, 'utilities-color.html')

def utilities_other(request):
    return render(request, 'utilities-other.html')
