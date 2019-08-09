from django.contrib import admin
from django.urls import path, include
from  . import views
urlpatterns = [
    path('login/', views.userlogin, name="userlogin" ),
    #path('signup/', views.signup, name="signup" ),
    path('logout/', views.logout, name="logout" ),
    #path('signupTest/', views.signupTest, name="signupTest" ),
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
    path('post_1', views.post_1, name="post_1"),
    path('post_2', views.post_2, name="post_2"),
    path('post_3', views.post_3, name="post_3"),
    path('post_4', views.post_4, name="post_4"),
    path('post_5', views.post_5, name="post_5"),
    path('post_6', views.post_6, name="post_6"),
    path('post_7', views.post_7, name="post_7"),
    path('post_8', views.post_8, name="post_8"),
    path('post_9', views.post_9, name="post_9"),
    path('post_10', views.post_10, name="post_10"),








]





