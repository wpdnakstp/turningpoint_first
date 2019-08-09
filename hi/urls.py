from django.contrib import admin
from django.urls import path, include
from  . import views
urlpatterns = [
    path('login/', views.userlogin, name="userlogin" ),
    #path('signup/', views.signup, name="signup" ),
    path('logout/', views.logout, name="logout" ),

    #path('signupTest/', views.signupTest, name="signupTest" ),
    path('intro_final', views.intro_final, name="intro_final"),
    #다이어리
    path('diary_ok', views.diary_ok, name="diary_ok"),
    path('diary_create',views.diary_create,name="diary_create"),
    path('diary_list', views.diary_list, name="diary_list"),
    path('diary_detail/<int:diary_id>',views.diary_detail,name="diary_detail"),
    #커뮤니티
    path('community_ok', views.community_ok, name="community_ok"),
    path('signup_ok', views.signup_ok, name="signup_ok"),
    path('password_ok', views.password_ok, name="password_ok"),
    path('book_make', views.book_make, name="book_make"),
    path('book_final', views.book_final, name="book_final"),
    path('todolist', views.todolist, name="todolist"),
    path('base_ok', views.base_ok, name="base_ok"),
    path('home', views.home, name="home"),
    path('post', views.post, name="post"),
    #종복체크
    path('id_overlap_check', views.id_overlap_check,name="id_overlap_check"),
    path('mailOverlapCheck', views.mailOverlapCheck,name="mailOverlapCheck"),
    path('nickOverlapCheck', views.nickOverlapCheck,name="nickOverlapCheck"),
    #중복체크
    path('ckid',views.ckid,name="ckid"),
    path('ckmail',views.ckmail,name="ckmail"),
    path('cknick',views.cknick,name="cknick"),
    #TodoList
    path('sTD',views.saveTodoList,name="sTD"),
    path('dTD',views.deleteTodoList,name="dTD"),
    path('cTD',views.checkTodoList,name="cTD"),




    path('signupTest/', views.signupTest, name="signupTest" ),
    path('intro_final/', views.intro_final, name="intro_final"),
    path('diary_ok/', views.diary_ok, name="diary_ok"),
    path('diary_list/', views.diary_list, name="diary_list"),

    path('community_ok/', views.community_ok, name="community_ok"),
    path('signup_ok/', views.signup_ok, name="signup_ok"),
    path('password_ok/', views.password_ok, name="password_ok"),
    path('book_make/', views.book_make, name="book_make"),
    path('book_final/', views.book_final, name="book_final"),
    path('todolist/', views.todolist, name="todolist"),
    path('post/', views.post, name="post"),

]


