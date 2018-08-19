from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request): #官網(內)
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })

def fullpage(request): #官網(外)
	return render(request,'index_fullpage.html',{

		})