from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Notice, Noticecomment, Free, Freecomment, Develop, Developcomment

# Create your views here.


# 공지사항

def notice(request):
    notices = Notice.objects
    return render(request, 'notice/notice.html',{'notices' : notices})

def noticedetail(request, notice_id):
    notice_detail = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'notice/noticedetail.html', {'notice' : notice_detail})

def noticenew(request):
    return render(request, 'notice/noticenew.html')

def noticecreate(request):
    notice = Notice()
    notice.title = request.GET['title']
    notice.body = request.GET['body']
    notice.pub_date = timezone.datetime.now()
    notice.save()
    return redirect('/board/notice/' + str(notice.id))

def noticedelete(request, notice_id):
    notice_delete = get_object_or_404(Notice,pk=notice_id)
    notice_delete.delete()
    return redirect('/board/notice/')

def noticeupdate(request,notice_id):
    notice_update=get_object_or_404(Notice,pk=notice_id)
    return render(request,'notice/noticeupdate.html',{"noticeupdate":notice_update})

def noticeupdatesend(request, notice_id):
    noticeupdatesend=get_object_or_404(Notice,pk=notice_id)
    noticeupdatesend.title=request.GET['updatetitle']
    noticeupdatesend.body=request.GET['updatebody']
    noticeupdatesend.pub_date=timezone.datetime.now() # 수정하면 그 시간으로 변경
    noticeupdatesend.save()
    return redirect('/board/notice/' + str(noticeupdatesend.id)) 

def noticecommentcreate(request, notice_id):
    notice=get_object_or_404(Notice, pk=notice_id) # 부모클래스의 아이디값을 가져와야한다 - 부모클래스에 종속시켜야 하기 때문에
    content = request.POST.get('content') # POST['comment'] 라고 하면 안된다!
    Noticecomment.objects.create(notice=notice,commentbody=content) # 새롭게 모델 안에 정보를 만든다 - 여기서 좌변은 models 안에 있는거, 우변은 def 안에 있는거
    return redirect('/board/notice/' + str(notice.id)) # 저 문자열 '/detail/<int:board.id>'라고 하면 안된다! 그냥 저렇게 하자


# 자유게시판

def free(request):
    frees = Free.objects
    return render(request, 'free/free.html',{'frees' : frees})

def freedetail(request, free_id):
    free_detail = get_object_or_404(Free, pk=free_id)
    return render(request, 'free/freedetail.html', {'free' : free_detail})

def freenew(request):
    return render(request, 'free/freenew.html')

def freecreate(request):
    free = Free()
    free.title = request.GET['title']
    free.body = request.GET['body']
    free.pub_date = timezone.datetime.now()
    free.save()
    return redirect('/board/free/' + str(free.id))

def freedelete(request, free_id):
    free_delete = get_object_or_404(Free,pk=free_id)
    free_delete.delete()
    return redirect('/board/free/')

def freeupdate(request,free_id):
    free_update=get_object_or_404(Free,pk=free_id)
    return render(request,'free/freeupdate.html',{"freeupdate":free_update})

def freeupdatesend(request, free_id):
    freeupdatesend=get_object_or_404(Free,pk=free_id)
    freeupdatesend.title=request.GET['updatetitle']
    freeupdatesend.body=request.GET['updatebody']
    freeupdatesend.pub_date=timezone.datetime.now() # 수정하면 그 시간으로 변경
    freeupdatesend.save()
    return redirect('/board/free/' + str(freeupdatesend.id))

def freecommentcreate(request, free_id):
    free=get_object_or_404(Free, pk=free_id) # 부모클래스의 아이디값을 가져와야한다 - 부모클래스에 종속시켜야 하기 때문에
    content = request.POST.get('content') # POST['comment'] 라고 하면 안된다!
    Freecomment.objects.create(free=free,commentbody=content) # 새롭게 모델 안에 정보를 만든다 - 여기서 좌변은 models 안에 있는거, 우변은 def 안에 있는거
    return redirect('/board/free/' + str(free.id)) # 저 문자열 '/detail/<int:board.id>'라고 하면 안된다! 그냥 저렇게 하자


# 자기계발게시판

def develop(request):
    develops = Develop.objects
    return render(request, 'develop/develop.html',{'develops' : develops})

def developdetail(request, develop_id):
    develop_detail = get_object_or_404(Develop, pk=develop_id)
    return render(request, 'develop/developdetail.html', {'develop' : develop_detail})

def developnew(request):
    return render(request, 'develop/developnew.html')

def developcreate(request):
    develop = Develop()
    develop.title = request.GET['title']
    develop.body = request.GET['body']
    develop.pub_date = timezone.datetime.now()
    develop.save()
    return redirect('/board/develop/' + str(develop.id))

def developdelete(request, develop_id):
    develop_delete = get_object_or_404(Develop,pk=develop_id)
    develop_delete.delete()
    return redirect('/board/develop/') 

def developupdate(request,develop_id):
    develop_update=get_object_or_404(Develop,pk=develop_id)
    return render(request,'develop/developupdate.html',{"developupdate":develop_update})

def developupdatesend(request, develop_id):
    developupdatesend=get_object_or_404(Develop,pk=develop_id)
    developupdatesend.title=request.GET['updatetitle']
    developupdatesend.body=request.GET['updatebody']
    developupdatesend.pub_date=timezone.datetime.now() # 수정하면 그 시간으로 변경
    developupdatesend.save()
    return redirect('/board/develop/' + str(developupdatesend.id))

def developcommentcreate(request, develop_id):
    develop=get_object_or_404(Develop, pk=develop_id) # 부모클래스의 아이디값을 가져와야한다 - 부모클래스에 종속시켜야 하기 때문에
    content = request.POST.get('content') # POST['comment'] 라고 하면 안된다!
    Developcomment.objects.create(develop=develop,commentbody=content) # 새롭게 모델 안에 정보를 만든다 - 여기서 좌변은 models 안에 있는거, 우변은 def 안에 있는거
    return redirect('/board/develop/' + str(develop.id)) # 저 문자열 '/detail/<int:board.id>'라고 하면 안된다! 그냥 저렇게 하자