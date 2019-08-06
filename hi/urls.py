from django.contrib import admin
from django.urls import path, include
from  . import views
urlpatterns = [
    path('login/', views.userlogin, name="userlogin" ),
    # path('signup/', views.signup, name="signup" ),
    path('logout/', views.logout, name="logout" ),
    # path('signupTest/', views.signupTest, name="signupTest" ),
    path('intro_final', views.intro_final, name="intro_final"),
    path('diary_ok', views.diary_ok, name="diary_ok"),
    path('community_ok', views.community_ok, name="community_ok"),
    path('signup_ok', views.signup_ok, name="signup_ok"),
    path('password_ok', views.password_ok, name="password_ok"),
    path('book_make', views.book_make, name="book_make"),
    path('book_final', views.book_final, name="book_final"),
    path('todolist', views.todolist, name="todolist"),
    path('diary_list', views.diary_list, name="diary_list"),
    path('base_ok', views.base_ok, name="base_ok"),
    path('home', views.home, name="home"),







]





