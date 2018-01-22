"""sapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from sappsapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^login/', login, name='login'),
    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^profile/', profile, name='profile'),
    url(r'^profileedit/', profileedit, name='profileedit'),
    url(r'^students/', students, name='students'),
    url(r'^attendance/', attendance, name='attendance'),
    url(r'^mcqs/', mcqs, name='mcqs'),
    url(r'^assignments/', assignments, name='assignments'),
    url(r'^resources/', resources, name='resources'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
