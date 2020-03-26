from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


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


def testpage_line(request):
    """LINE LOGIN測試頁面"""
    return render(request, 'inner_template/line_test.html', {
    })


def testpage_lineliff(request):
    """LINE LIFF測試頁面"""
    return render(request, 'inner_template/line_liff.html', {
    })


def testpage_redirect(request):
    """重新導向頁面"""
    url = request.GET.get("url")
    return HttpResponseRedirect(f"https://{url}")
