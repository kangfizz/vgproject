from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })
