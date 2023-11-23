# example/urls.py
from django.urls import path

from example.views import index

urlpatterns = [
    path('', index),
    path('hola', index),
]







# example/urls.py
from django.urls import path

from example.views import (
    index,
    not_found,
    blank,
    buttons,
    cards,
    charts,
    forgot_password,
    user_login,
    register,
    tables,
    utilities_animation,
    utilities_border,
    utilities_color,
    utilities_other,
)

urlpatterns = [
    path('index.html', index),
    path('hola', index),
    path('404.html', not_found),
    path('blank.html', blank),
    path('buttons.html', buttons),
    path('cards.html', cards),
    path('charts.html', charts),
    path('forgot-password.html', forgot_password),
    path('login.html', user_login),
    path('register.html', register),
    path('tables.html', tables),
    path('utilities-animation.html', utilities_animation),
    path('utilities-border.html', utilities_border),
    path('utilities-color.html', utilities_color),
    path('utilities-other.html', utilities_other),
]
