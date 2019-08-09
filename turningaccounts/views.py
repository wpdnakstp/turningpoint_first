from django.shortcuts import render
from . models import TurningUser

# Create your views here.

#ID 찾기
def fid(request):
  return render(request,'fid.html')


#비밀번호 찾기
def fpw(request):
  return render(request,'fpw.html')


#아이디 찾기 알고리즘
def searchid(request):
  realUserId = TurningUser.objects.all()
  realUserId = realUserId.filter(username=request.POST.get("findName")) 
  realUserId = realUserId.filter(email=request.POST.get("findEmail"))
  return render(request,"searchid.html",{"testQuerySet":realUserId})


# def test(request):
#   return render(request,"test.html")

# #비밀번호 찾기 알고리즘
# def searchpw(request):
#   realUserPw = TurningUser.objects.all()
#   realUserPw = realUserPw.filter(username=request.POST.get("findName")) 
#   realUserPw = realUserPw.filter(email=request.POST.get("findEmail"))
#   realUserPw = realUserPw.filter(nickName=request.POST.get("findNickName"))
#   return render(request,"searchpw.html",{"testQuerySet":realUserPw})

# def changePW(request):
#   return redirect('pr')