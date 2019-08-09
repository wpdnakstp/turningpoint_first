from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
  path('fid/', views.fid, name="fid"),
  path('fpw/', views.fpw, name="fpw"),
  #절대주소 사용법 - 아이디 및 비밀번호 찾기
   path('/searchid/',views.searchid, name="searchid"),
  # path('/searchpw/',views.searchpw, name="searchpw"),
  # path('/chpw/',views.changePW,name="changePW"),
  # path('test/',views.test,name="test"),
]
