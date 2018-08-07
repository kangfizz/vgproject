# echobot/urls.py

# from captcha_admin import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^hello/', views.hello_world),
]
