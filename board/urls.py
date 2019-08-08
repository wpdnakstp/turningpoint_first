from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    # 공지사항 - Notice
    path('notice/', views.notice, name="notice" ),
    path('notice/<int:notice_id>', views.noticedetail, name="noticedetail"),
    path('notice/new/', views.noticenew, name="noticenew"),
    path('notice/create/', views.noticecreate, name="noticecreate"),
    path('notice/delete/<int:notice_id>', views.noticedelete, name='noticedelete'),
    path('notice/update/<int:notice_id>', views.noticeupdate, name='noticeupdate'),
    path('notice/updatesend/<int:notice_id>', views.noticeupdatesend, name='noticeupdatesend'),
    path('notice/<int:notice_id>/commentcreate', views.noticecommentcreate, name='noticecommentcreate'),
    path('notice/<int:notice_id>/noticeLike',views.noticeLike,name="noticeLike"),
    path('notice/deletecomment/<int:notice_id>', views.noticecommentdelete, name='noticecommentdelete'),
    path('notice/search', views.notice_list, name="noticelist"),

    # path('notice/<int:notice_id>/like', views.like, name="noticelike"),
    # path('notice/test',views.test,name="test"),

    # 자유게시판 - Free
    path('free/', views.free, name="free" ),
    path('free/<int:free_id>', views.freedetail, name="freedetail"),
    path('free/new/', views.freenew, name="freenew"),
    path('free/create/', views.freecreate, name="freecreate"),
    path('free/delete/<int:free_id>', views.freedelete, name='freedelete'),
    path('free/update/<int:free_id>', views.freeupdate, name='freeupdate'),
    path('free/updatesend/<int:free_id>', views.freeupdatesend, name='freeupdatesend'),
    path('free/<int:free_id>/commentcreate', views.freecommentcreate, name='freecommentcreate'),
    path('free/<int:free_id>/freeLike',views.freeLike,name="freeLike"),
    path('free/deletecomment/<int:free_id>', views.freecommentdelete, name='freecommentdelete'),
    path('free/search', views.free_list, name="freelist"),
    
    # 자기계발게시판 - Develop
    path('develop/', views.develop, name="develop" ),
    path('develop/<int:develop_id>', views.developdetail, name="developdetail"),
    path('develop/new/', views.developnew, name="developnew"),
    path('develop/create/', views.developcreate, name="developcreate"),
    path('develop/delete/<int:develop_id>', views.developdelete, name='developdelete'),
    path('develop/update/<int:develop_id>', views.developupdate, name='developupdate'),
    path('develop/updatesend/<int:develop_id>', views.developupdatesend, name='developupdatesend'),
    path('develop/<int:develop_id>/commentcreate', views.developcommentcreate, name='developcommentcreate'),
    path('develop/<int:develop_id>/developLike',views.developLike,name="developLike"),
    path('develop/deletecomment/<int:develop_id>', views.developcommentdelete, name='developcommentdelete'),
    path('develop/search', views.develop_list, name="developlist"),

]