# inner_database/urls.py

# from captcha_admin import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^index/', views.index),
    url('^test_facebook/', views.testpage),
    url('^test_line/', views.testpage_line),
    url('^test_line_liff/', views.testpage_lineliff),
]
