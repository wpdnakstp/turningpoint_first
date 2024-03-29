from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User   # User모델을 import했어요!
from django.contrib import auth  # auth라는 모듈도 import합니다. 서버로 넘어온 유저 데이터를 처리하는 역할을 할거에요!
from django.core.paginator import Paginator
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
#TurningUser > Model of turningaccounts > other app
from turningaccounts.models import TurningUser
from datetime import datetime
#email validation check import re
import re

# Create your views here.

def home(request):
    return render(request, 'home.html')

def pr(request):
    return render(request, 'pr.html')

def userlogin(request):   # userlogin으로 꼭 안하셔도 되고 login등등으로 마음껏 하셔도 됩니다!
    if request.method == 'POST':     # 앞에서 설명한대로 유저 정보는 노출되면 안되기 때문에 POST 메서드를 사용해 유저가 입력한 로그인 정보를 서버로 보내줬어요!
        username = request.POST['username']  # request에 담겨온 데이터 중 username의 데이터를 username변수에 담아줬어요!
        password = request.POST['password']  # 마찬가지로 password데이터를 password변수에 담아줍니다
        user = auth.authenticate(request, username = username, password = password) 
					# auth모듈에 내장된 authenticate메서드는 request(요청)을 인자로 받고, 우리가 사용자로부터 받은 username,password를 User모델 데이터들 중에서 일치하는 유저를 가져다 user변수에 담아줍니다.
        if user is not None:  # 그래서 사용자가 보낸 데이터가 User테이블의 데이터와 일치하는게 있으면, 그걸 user변수에 담아줄거고, 그 user변수가 None이 아닐 때, 즉 유저가 있을 때를 여기서 처리합니다.
            auth.login(request, user)  # auth모듈의 login메서드를 통해 위에서 가져온 user를 로그인 처리합니다.
            return redirect('mypage') # 그리고 로그인이 정상적으로 되면 index페이지로 리다이렉트 시켜주죠!
        else :
            return render(request, 'intro_final.html', {'error':'username or password is incorrect'}) # 만약에 위에서 user변수에 아무 유저도 담기지 않았다면, 즉 로그인 정보가 유효하지 않으면 화면을 넘기지 않고 메시지를 띄워줍니다.
    else :  # 요청이 POST방식이 아니라면, 즉 로그인 페이지에 들어오는 get방식의 요청이 있을 때
        return render(request, 'intro_final.html') # 로그인 화면을 띄워주는 html을 렌더링 해줍니다.
    # return render(request, 'intro_final.html')

# def signup(request): # 회원가입 함수입니다.
#     if request.method == 'POST':   # POST방식일 때, 즉 서버로 데이터가 넘겨졌을 때(사용자가 회원가입 정보를 입력하고 가입하기를 눌렀을 때) 아래 함수를 실행합니다.
#         if request.POST['password1'] == request.POST['password2']: # 우리가 '비밀번호'와 '비밀번호 확인' 두 개의 데이터를 받아 이 두 항목이 일치할 때 회원가입을 진행시켜줄거에요!
#             user = TurningUser.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
# 						# 비밀번호 확인이 되면, 넘어온 회원가입 데이터를 가지고 User모델에 유저 데이터를 생성해줍니다.
#             auth.login(request, user) # 그리고 회원가입이 성공적으로 수행된 후에 자동으로 로그인을 한번 해줍니다.
#             return redirect('intro_final')
#     return render(request, 'intro_final.html') # Post방식이 아닌 get방식일 경우 회원가입창을 띄워줍니다.






# #Custom Model Signup Test 
# def signupTest(request): 
#     if request.method == 'POST':
#         userNickName = request.POST['nickName']
#         originPW = request.POST['password1']
#         checkPW = request.POST['password2']
#         userName = request.POST['username']
#         userEmail = request.POST['trEmail']
#         userArmyStatus = request.POST['selectArmy']
#         userPhoneNumb = request.POST.get('phonenumber','')
#         #for checking email validation
#         emailValidation = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
#         #for checking phoneNumber
#         phoneNumb = re.compile('\d{3}-\d{4}-\d{4}')
#         if emailValidation.match(userEmail) == None:
#             return render(request,'signupTest.html',{"error":"올바른 이메일 형식이 아닙니다."})
#         else:
#             if phoneNumb.match(userPhoneNumb) == None:
#                 return render(request,'signupTest.html',{"error":"올바른 전화번호 형식이 아닙니다."})
#             if originPW == checkPW:
#                 try:
#                     tnUser = TurningUser.objects.get(nickName=userNickName)
#                     return render(request, 'signupTest.html',{"error":"이미 가입된 닉네임 입니다."})
#                 except TurningUser.DoesNotExist:
#                     tnUser = TurningUser.objects.create_user(
#                         userName,
#                         userEmail,
#                         password=originPW,
#                         nickName=userNickName,
#                         tnPhoneNumb=userPhoneNumb
#                     )
#                     auth.login(request,tnUser)
#                     return redirect('pr')
#             else:
#                 return render(request,'signupTest.html',{"error":"비밀번호가 같지 않습니다."})
#     else:
#         return render(request,'signupTest.html')


#     return render(request,'signupTest.html')



def logout(request):
    auth.logout(request)
    return redirect('intro_final')


def dd(request):
    return render(request, 'dd.html')

def calender(request):
    return render(request, 'calender.html')

def mypage(request):
    return render(request, 'mypage.html')

def intro_final(request):
    return render(request, 'intro_final.html')


def diary_ok(request):
    return render(request, 'diary/diary_ok.html')

def community_ok(request):
    return render(request, 'community/community_ok.html')

def signup_ok(request):
    todayYear = datetime.today().year
    todayYearList = []
    for i in range(1,101):
        a = todayYear + i
        b = todayYear - i
        todayYearList.append(a)
        todayYearList.append(b)
    todayYearList.append(todayYear)
    todayYearList.sort()
    if request.method == "POST":
        userId = request.POST.get('username')
        realPW = request.POST.get('password1')
        checkPW = request.POST.get('password2')
        userName = request.POST.get('full_name')
        birthDay = str(request.POST.get('birth_year'))+str(request.POST.get('birth_mon'))+str(request.POST.get('birth_day'))
        userGender = request.POST.get('gender')
        userNickName = request.POST.get('nickName')
        userEmail = request.POST.get('email')
        phoneNumb = str(request.POST.get('phoneFirst'))+"-"+str(request.POST.get('phoneMiddle'))+"-"+str(request.POST.get('phoneLast'))
        userArmy = request.POST.get('userArmy')
        #유효성 검사
        emailValidation = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        phoneNumbValidation = re.compile('\d{3}-\d{4}-\d{4}')
        if emailValidation.match(userEmail) == None:
            return render(request,'signup_ok.html',{"error":"올바른 이메일 형식이 아닙니다."})
        elif phoneNumbValidation.match(phoneNumb) == None:
            return render(request,'signup_ok.html',{"error":"올바른 휴대폰 형식이 아닙니다."})
        else:
            if realPW == checkPW:
                try:
                    tnUser = TurningUser.objects.get(username=userId)
                    return render(request, 'signup_ok.html',{"error":"이미 가입된 아이디 입니다."})
                except TurningUser.DoesNotExist:
                    tnUser = TurningUser.objects.create_user(
                        userId,
                        userEmail,
                        password=realPW,
                        nickName=userNickName,
                        userFullName=userName,
                        userGender=userGender,
                        tnPhoneNumb=phoneNumb,
                        userArmyName=userArmy,
                        userBirthDay=birthDay
                    )
                    auth.login(request,tnUser)
                    return redirect('mypage')
            else:
                return render(request,'signup_ok.html',{"error":"비밀번호가 같지 않습니다."})
    return render(request, 'signup_ok.html',{"year":todayYearList})


def password_ok(request):
    return render(request, 'password_ok.html')

def book_make(request):
    return render(request, 'diary/book_make.html')

def book_final(request):
    return render(request, 'diary/book_final.html')

def todolist(request):
    return render(request, 'todolist.html')


def diary_list(request):
    return render(request, 'diary/diary_list.html')

def base_ok(request):
    return render(request, 'base_ok.html')