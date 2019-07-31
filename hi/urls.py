from django.contrib import admin
from django.urls import path, include
from  . import views
urlpatterns = [
    path('login/', views.userlogin, name="login" ),
    path('signup/', views.signup, name="signup" ),
    path('logout/', views.logout, name="logout" ),
    path('signupTest/', views.signupTest, name="signupTest" ),
    path('intro_final', views.intro_final, name="intro_final"),
    path('diary_ok', views.diary_ok, name="diary_ok"),
    path('community_ok', views.community_ok, name="community_ok"),
]
