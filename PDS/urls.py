"""PDS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from mainapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    url('^admin/',admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^venlogin/$',views.ven_login,name='ven_login'),
    url(r'^Packlogin/$',views.Pack_login,name='Pack_login'),
    url(r'^requestreturn/(?P<pk>\d+)/$',views.request_return,name='request_return'),
    url(r'^checkreturn/(?P<pk>\d+)/$',views.check_return,name='check_return'),
    url(r'^venHome/(?P<pk>\d+)/$',views.ven_Home,name='ven_Home'),
    url(r'^PackHome/(?P<pk>\d+)/$',views.Pack_Home,name='Pack_Home'),
]

