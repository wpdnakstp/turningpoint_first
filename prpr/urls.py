"""prpr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

from django.contrib import admin
from django.urls import path, include
import hi.views
import cal.views
import cal.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hi.views.intro_final, name="intro_final"),
    path('hi/', include('hi.urls')),
    path('dd/', hi.views.dd, name="dd"),
    # path('calender/', hi.views.calender, name="calender"),
    path('mypage/', hi.views.mypage, name="mypage"),
    path('board/', include('board.urls')), # board쪽으로 url 연결
    #turningaccounts url
    path('turningaccounts/',include('turningaccounts.urls')),
    path('cal/', include('cal.urls')),
    url(r'^calendar/$', cal.views.CalendarView.as_view(), name='calendar'),


]
