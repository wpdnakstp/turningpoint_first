from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Notice, Noticecomment, Free, Freecomment, Develop, Developcomment
from turningaccounts.models import TurningUser

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.


# 공지사항

def notice(request):
    notices = Notice.objects
    notices_list = Notice.objects.all().order_by('-id')
    paginator = Paginator(notices_list,15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'notice/notice.html', {'notices' : notices,'posts' : posts})

def noticedetail(request, notice_id):
    notice_detail = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'notice/noticedetail.html', {'notice' : notice_detail})

def noticenew(request):
  notices = Notice.objects
  #관리자 계정이 아니면 글쓰기 불가능
  if request.user.is_superuser:
    return render(request, 'notice/noticenew.html')
  else:
    error = "권한이 없습니다."
    # return render(request,"notice/notice.html",{"error":"권한이 없습니다."})
    return render(request,'notice/notice.html',{"error":error,"notices":notices})


def noticecreate(request):
    notice = Notice()
    #tnUser라는 테이블 값에 현재 request를 보내는 User값을 넣어줌
    notice.tnUser = request.user
    notice.title = request.GET['title']
    notice.body = request.GET['body']
    notice.pub_date = timezone.datetime.now()
    notice.save()
    return redirect('/board/notice/' + str(notice.id))

def noticedelete(request, notice_id):
    notice_delete = get_object_or_404(Notice,pk=notice_id)
    #진짜 글 소유주 유저값 > 유저 값 queryset pk값을 꼭 참고하도록
    realUser = notice_delete.tnUser
    #현재 로그인되어있는 user값
    nowUser = request.user
    #유저 값이 같을 때 삭제할 수 있도록
    if nowUser == realUser:
      notice_delete.delete()
      return redirect('/board/notice/')
    else:
      return redirect('/board/notice/'+str(notice_id))
      # return render(request,'notice/notice.html',{"error":"id값이 다릅니다."} )


def noticeupdate(request,notice_id):
    notice_update=get_object_or_404(Notice,pk=notice_id)
    nowUser = request.user
    realUser = notice_update.tnUser
    #유저의 아이디값이 같아야 수정할 수 있도록 바꿈
    if nowUser == realUser:
      return render(request,'notice/noticeupdate.html',{"noticeupdate":notice_update})
    else:
      return redirect('/board/notice/'+str(notice_id))
      # return render(request,'/board/notice/'+str(notice_id),{"error":"수정권한이 없습니다."})

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
    #tnUser라는 테이블 값에 현재 request를 보내는 User값을 넣어줌
    Noticecomment.objects.create(notice=notice,commentbody=content,noticeCommentUser=request.user) # 새롭게 모델 안에 정보를 만든다 - 여기서 좌변은 models 안에 있는거, 우변은 def 안에 있는거
    return redirect('/board/notice/' + str(notice.id)) # 저 문자열 '/detail/<int:board.id>'라고 하면 안된다! 그냥 저렇게 하자

def noticecommentdelete(request, notice_id):
    notice_delete = get_object_or_404(Noticecomment,pk=notice_id)
    post_id = notice_delete.notice.pk
    #진짜 글 소유주 유저값 > 유저 값 queryset pk값을 꼭 참고하도록
    realUser = notice_delete.noticeCommentUser
    #현재 로그인되어있는 user값
    nowUser = request.user
    #유저 값이 같을 때 삭제할 수 있도록
    if nowUser == realUser:
      notice_delete.delete()
      return redirect('/board/notice/'+str(post_id))
    else:
      return redirect('/board/notice/'+str(post_id))
      # return render(request,'notice/notice.html',{"error":"id값이 다릅니다."} )

#좋아요 기능 구현
def noticeLike(request,notice_id):
  #POST 형식일 때
  if request.method=="POST":
    #현재 user 상태
    user = request.user
    #free라는 변수에, Free 모델의 free_id값을 pk로 가지는 queryset 저장
    notice = Notice.objects.get(pk=notice_id)
    #테스트용 free class의 totalLike 함수 불러오기
    aaa = notice.totalLike
    #만약 Free 모델의 userLikeName 항목에서 filter값이 id=user.id값이 존재한다면
    #user.id -> 각 유저모델이 만들어질때, 발생하는 특정 값
    if notice.userLikeName.filter(id=user.id).exists():
      #Free 모델의 다대다 함수에서 user를 삭제 > 빼기
      notice.userLikeName.remove(user)
      error = "좋아요를 취소합니다."
      return redirect('/board/notice/'+str(notice_id))
      # return render(request,'free/ttest.html',{"message":error,"aaa":aaa})
    else:
      #만약 Free User model에서 다대다 관계에 해당 user값이 없으면 queryset에 추가할 것
      notice.userLikeName.add(user)
      error = "좋아요를 누릅니다."
      # return render(request,'free/ttest.html',{"message":error,"aaa":aaa})
      return redirect('/board/notice/'+str(notice_id))

def notice_list(request):
    qs = Notice.objects.all().order_by('-id')
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링

    paginator = Paginator(qs,15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    return render(request, 'notice/noticesearch.html', {
        'post_list' : qs,
        'q' : q,
        'posts' : posts,
    })


# 자유게시판

def free(request):
    frees = Free.objects
    frees_list = Free.objects.all().order_by('-id')
    paginator = Paginator(frees_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'free/free.html',{'frees' : frees,'posts':posts})

def freedetail(request, free_id):
    free_detail = get_object_or_404(Free, pk=free_id)
    return render(request, 'free/freedetail.html', {'free' : free_detail})

def freenew(request):
    #User 로그인이 안되었을 경우에, 글쓰기 버튼을 누르면 error 처리
    if request.user.is_authenticated:
      
      return render(request, 'free/freenew.html')
    else:
      return render(request,"free/free.html",{"error":"로그인이 필요합니다."})

#좋아요 기능 구현
def freeLike(request,free_id):
  #POST 형식일 때
  if request.method=="POST":
    #현재 user 상태
    user = request.user
    #free라는 변수에, Free 모델의 free_id값을 pk로 가지는 queryset 저장
    free = Free.objects.get(pk=free_id)
    #테스트용 free class의 totalLike 함수 불러오기
    aaa = free.totalLike
    #만약 Free 모델의 userLikeName 항목에서 filter값이 id=user.id값이 존재한다면
    #user.id -> 각 유저모델이 만들어질때, 발생하는 특정 값
    if free.userLikeName.filter(id=user.id).exists():
      #Free 모델의 다대다 함수에서 user를 삭제 > 빼기
      free.userLikeName.remove(user)
      error = "좋아요를 취소합니다."
      return redirect('/board/free/'+str(free_id))
      # return render(request,'free/ttest.html',{"message":error,"aaa":aaa})
    else:
      #만약 Free User model에서 다대다 관계에 해당 user값이 없으면 queryset에 추가할 것
      free.userLikeName.add(user)
      error = "좋아요를 누릅니다."
      # return render(request,'free/ttest.html',{"message":error,"aaa":aaa})
      return redirect('/board/free/'+str(free_id))

def freecreate(request):
    free = Free()
    #글 소유주 설정
    free.tnUser = request.user
    free.title = request.GET['title']
    free.body = request.GET['body']
    free.pub_date = timezone.datetime.now()
    free.save()
    return redirect('/board/free/' + str(free.id))

def freedelete(request, free_id):
  #유저값 확인한 다음에 지워주는 기능 추가
    free_delete = get_object_or_404(Free,pk=free_id)
    nowUser = request.user
    realUser = free_delete.tnUser
    if nowUser == realUser:
      free_delete.delete()
      return redirect('/board/free/')
    else:
      return redirect('/board/free/'+str(free_id)) 



def freeupdate(request,free_id):
  #유저값 확인 후 수정 가능
    free_update=get_object_or_404(Free,pk=free_id)
    nowUser = request.user
    realUser = free_update.tnUser
    if nowUser == realUser:
      return render(request,'free/freeupdate.html',{"freeupdate":free_update})
    else:
      return redirect('/board/free/'+str(free_id))



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
    Freecomment.objects.create(free=free,commentbody=content,tnFreeCommentUser=request.user) # 새롭게 모델 안에 정보를 만든다 - 여기서 좌변은 models 안에 있는거, 우변은 def 안에 있는거
    return redirect('/board/free/' + str(free.id)) # 저 문자열 '/detail/<int:board.id>'라고 하면 안된다! 그냥 저렇게 하자

def freecommentdelete(request, free_id):
  #유저값 확인한 다음에 지워주는 기능 추가
    free_delete = get_object_or_404(Freecomment,pk=free_id)
    post_id = free_delete.free.pk
    nowUser = request.user
    realUser = free_delete.tnFreeCommentUser
    if nowUser == realUser:
      free_delete.delete()
      return redirect('/board/free/'+str(post_id))
    else:
      return redirect('/board/free/'+str(post_id))

def free_list(request):
    qs = Free.objects.all().order_by('-id')
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링

    paginator = Paginator(qs,15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    return render(request, 'free/freesearch.html', {
        'post_list' : qs,
        'q' : q,
        'posts' : posts,
    })



# 자기계발게시판

def develop(request):
    develops = Develop.objects
    develops_list = Develop.objects.all().order_by('-id')
    paginator = Paginator(develops_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'develop/develop.html',{'develops' : develops, 'posts':posts})

def developdetail(request, develop_id):
    develop_detail = get_object_or_404(Develop, pk=develop_id)
    return render(request, 'develop/developdetail.html', {'develop' : develop_detail})

def developnew(request):
    if request.user.is_authenticated:
      return render(request, 'develop/developnew.html')
    else:
      return render(request,'develop/develop.html',{"error":"로그인이 필요합니다."})



def developcreate(request):
    develop = Develop()
    develop.tnUser = request.user
    develop.title = request.GET['title']
    develop.body = request.GET['body']
    develop.pub_date = timezone.datetime.now()
    develop.save()
    return redirect('/board/develop/' + str(develop.id))

def developdelete(request, develop_id):
    #User 아이디 값 확인한 다음에 자기계발 지울수 있게 하기
    develop_delete = get_object_or_404(Develop,pk=develop_id)
    post_id = develop_delete.develop.pk
    nowUser = request.user
    realUser = develop_delete.tnUser
    if nowUser == realUser:
      develop_delete.delete()
      return redirect('/board/develop/')
    else:
      return redirect('/board/develop/'+str(develop_id))

def developupdate(request,develop_id):
    #유저 아이디 값 확인한 다음에 자기계발 수정할 수 있도록 만들었음
    develop_update=get_object_or_404(Develop,pk=develop_id)
    nowUser = request.user
    realUser = develop_update.tnUser
    if nowUser == realUser:
      return render(request,'develop/developupdate.html',{"developupdate":develop_update})
    else:
      return redirect('board/develop/'+str(develop_id))

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
    Developcomment.objects.create(develop=develop,commentbody=content,tnDevelopCommentUser=request.user) # 새롭게 모델 안에 정보를 만든다 - 여기서 좌변은 models 안에 있는거, 우변은 def 안에 있는거
    return redirect('/board/develop/' + str(develop.id)) # 저 문자열 '/detail/<int:board.id>'라고 하면 안된다! 그냥 저렇게 하자

def developcommentdelete(request, develop_id):
    #User 아이디 값 확인한 다음에 자기계발 지울수 있게 하기
    develop_delete = get_object_or_404(Developcomment,pk=develop_id)
    post_id = develop_delete.develop.pk
    nowUser = request.user
    realUser = develop_delete.tnDevelopCommentUser
    if nowUser == realUser:
      develop_delete.delete()
      return redirect('/board/develop/'+str(post_id))
    else:
      return redirect('/board/develop/'+str(post_id))

#좋아요 기능 구현
def developLike(request,develop_id):
  #POST 형식일 때
  if request.method=="POST":
    #현재 user 상태
    user = request.user
    #free라는 변수에, Free 모델의 free_id값을 pk로 가지는 queryset 저장
    develop = Develop.objects.get(pk=develop_id)
    #테스트용 free class의 totalLike 함수 불러오기
    aaa = develop.totalLike
    #만약 Free 모델의 userLikeName 항목에서 filter값이 id=user.id값이 존재한다면
    #user.id -> 각 유저모델이 만들어질때, 발생하는 특정 값
    if develop.userLikeName.filter(id=user.id).exists():
      #Free 모델의 다대다 함수에서 user를 삭제 > 빼기
      develop.userLikeName.remove(user)
      error = "좋아요를 취소합니다."
      return redirect('/board/develop/'+str(develop_id))
      # return render(request,'free/ttest.html',{"message":error,"aaa":aaa})
    else:
      #만약 Free User model에서 다대다 관계에 해당 user값이 없으면 queryset에 추가할 것
      develop.userLikeName.add(user)
      error = "좋아요를 누릅니다."
      # return render(request,'free/ttest.html',{"message":error,"aaa":aaa})
      return redirect('/board/develop/'+str(develop_id))

def develop_list(request):
    qs = Develop.objects.all().order_by('-id')
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링

    paginator = Paginator(qs,15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    return render(request, 'develop/developsearch.html', {
        'post_list' : qs,
        'q' : q,
        'posts' : posts,
    })






# # 좋아요
# @login_required
# def like(request,notice_id):
#     post=get_object_or_404(Notice, pk = notice_id)
#     if Notice.objects.filter(userLike=request.user.userLike).exists():
#       post.likePoint.remove(request.user)
#     else:
#         post.likePoint.add(request.user)
#     post.save()
#     return redirect('/board/notice/'+str(notice_id))
#     # return render(request,'notice/test.html', {"set":post.userLike})


# def test(request):
#   return render(request,'notice/test.html')