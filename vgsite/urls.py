"""vgsite URL Configuration

"""
import django
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from offwebsite import views as oviews

urlpatterns = [
    url(r'^$', oviews.fullpage),
    url(r'^admin/', admin.site.urls),
    url(r'^vgsite/', include('offwebsite.urls')),
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
