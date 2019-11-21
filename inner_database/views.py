from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    """官網（內)"""
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })

def testpage(request):
    """FB測試頁面"""
    return render(request, 'inner_template/FB_test.html', {
    })