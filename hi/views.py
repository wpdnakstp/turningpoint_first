from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User   # User모델을 import했어요!
from django.contrib import auth  # auth라는 모듈도 import합니다. 서버로 넘어온 유저 데이터를 처리하는 역할을 할거에요!
from django.core.paginator import Paginator
from django.utils import timezone
from .models import DiaryForm, Todolist
from django.core.files.storage import FileSystemStorage
#TurningUser > Model of turningaccounts > other app
from turningaccounts.models import TurningUser
from datetime import datetime
#email validation check import re
import re
from django.http import JsonResponse, HttpResponse

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
    return render(request, 'intro_final.html')

def signup(request): # 회원가입 함수입니다.
    if request.method == 'POST':   # POST방식일 때, 즉 서버로 데이터가 넘겨졌을 때(사용자가 회원가입 정보를 입력하고 가입하기를 눌렀을 때) 아래 함수를 실행합니다.
        if request.POST['password1'] == request.POST['password2']: # 우리가 '비밀번호'와 '비밀번호 확인' 두 개의 데이터를 받아 이 두 항목이 일치할 때 회원가입을 진행시켜줄거에요!
            user = TurningUser.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
						# 비밀번호 확인이 되면, 넘어온 회원가입 데이터를 가지고 User모델에 유저 데이터를 생성해줍니다.
            auth.login(request, user) # 그리고 회원가입이 성공적으로 수행된 후에 자동으로 로그인을 한번 해줍니다.
            return redirect('intro_final')
    return render(request, 'intro_final.html') # Post방식이 아닌 get방식일 경우 회원가입창을 띄워줍니다.


#Custom Model Signup Test 
def signupTest(request): 
    if request.method == 'POST':
        userNickName = request.POST['nickName']
        originPW = request.POST['password1']
        checkPW = request.POST['password2']
        userName = request.POST['username']
        userEmail = request.POST['trEmail']
        userArmyStatus = request.POST['selectArmy']
        userPhoneNumb = request.POST.get('phonenumber','')
        userLikeName = userName
        #for checking email validation
        emailValidation = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        #for checking phoneNumber
        phoneNumb = re.compile('\d{3}-\d{4}-\d{4}')
        if emailValidation.match(userEmail) == None:
            return render(request,'signupTest.html',{"error":"올바른 이메일 형식이 아닙니다."})
        else:
            if phoneNumb.match(userPhoneNumb) == None:
                return render(request,'signupTest.html',{"error":"올바른 전화번호 형식이 아닙니다."})
            if originPW == checkPW:
                try:
                    tnUser = TurningUser.objects.get(nickName=userNickName)
                    return render(request, 'signupTest.html',{"error":"이미 가입된 닉네임 입니다."})
                except TurningUser.DoesNotExist:
                    tnUser = TurningUser.objects.create_user(
                        userName,
                        userEmail,
                        password=originPW,
                        nickName=userNickName,
                        tnPhoneNumb=userPhoneNumb,
                        userLike = userLikeName
                    )
                    auth.login(request,tnUser)
                    return redirect('pr')
            else:
                return render(request,'signupTest.html',{"error":"비밀번호가 같지 않습니다."})
    else:
        return render(request,'signupTest.html')


    return render(request,'signupTest.html')



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
    if request.user != None:
        userDiary = DiaryForm.objects.count()
        pageNumb = userDiary
        pagePortion = (pageNumb-100)//50
        if pagePortion < 2:
            pagePrice = 10000
        else:
            pagePrice = 10000 + pagePortion*5000
    return render(request, 'diary/book_make.html',{"allDiary":userDiary,"pagePrice":pagePrice})

def book_final(request):
    return render(request, 'diary/book_final.html')

def todolist(request):
    printTodo = Todolist.objects.all()
    return render(request, 'todolist.html',{"todoList":printTodo})



#일기쓰기 views.py 함수들
def diary_ok(request):
    return render(request, 'diary/diary_ok.html')

def diary_create(request):
    diaryPost = DiaryForm()
    if request.method == 'POST':
        diaryPost.tnUser = request.user
        diaryPost.diaryBody = request.POST.get('text')
        diaryPost.diaryDate = request.POST.get('date')
        diaryPost.save()
        return redirect('diary_list')


        

    return render(request, 'diary/diary_list.html')


def diary_list(request):
    allDiary = DiaryForm.objects.all()
    return render(request, 'diary/diary_list.html',{"diary":allDiary})

def diary_detail(request,diary_id):
    diaryDetail = get_object_or_404(DiaryForm,pk=diary_id)
    return render(request, 'diary/diary_detail.html',{'diaryDetail':diaryDetail})

def base_ok(request):
    return render(request, 'base_ok.html')


def post_1(request):
    return render(request, 'blog/blogpost_1.html')

def post_2(request):
    return render(request, 'blog/blogpost_2.html')

def post_3(request):
    return render(request, 'blog/blogpost_3.html')

def post_4(request):
    return render(request, 'blog/blogpost_4.html')

def post_5(request):
    return render(request, 'blog/blogpost_5.html')


def post_6(request):
    return render(request, 'blog/blogpost_6.html')

def post_7(request):
    return render(request, 'blog/blogpost_7.html')


def post_8(request):
    return render(request, 'blog/blogpost_8.html')

def post_9(request):
    return render(request, 'blog/blogpost_9.html')

def post_10(request):
    return render(request, 'blog/blogpost_10.html')




def ckid(request):
    ckUserId = request.POST.get('test')
    if ckUserId == "":
        return render(request,'signup_ok.html',{"error":"아이디를 입력해주세요."})
    try:
        ckValId = TurningUser.objects.get(username=ckUserId)
        checkIdMent = "아이디가 중복되었습니다."
    except:
        checkIdMent = "아이디를 사용하실 수 있습니다."
    return HttpResponse(checkIdMent)


def ckmail(request):
    ckUserEmail = request.POST.get('testEmail')
    if ckUserEmail == "":
        return render(request,'signup_ok.html',{"error":"이메일을 입력해주세요."})
    try:
        ckMailValid = TurningUser.objects.get(email=ckUserEmail)
        checkEmailMent = "이메일이 중복되었습니다."
    except:
        checkEmailMent = "이메일을 사용하실 수 있습니다."
    return HttpResponse(checkEmailMent)

    
def cknick(request):
    ckUserNick = request.POST.get('testNick')
    if ckUserNick == "":
        return render(request,'signup_ok.html',{"error":"닉네임을 입력해주세요."})
    else:
        try:
            ckNickValid = TurningUser.objects.get(nickName=ckUserNick)
            checkNickMent = "닉네임이 중복되었습니다."
        except:
            checkNickMent = "닉네임을 사용하실 수 있습니다."
        return HttpResponse(checkNickMent)


# 아이디 중복검사 시작


def id_overlap_check(request):
    username = request.GET.get('username')
    try:
        #중복 검사 실패
        user = TurningUser.objects.get(username=username)
    except:
        #중복 검사 성공
        user = None
    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {"overlap":overlap}
    return JsonResponse(context)

def mailOverlapCheck(request):
    usermail = request.GET.get('usermail')
    try:
        userEmail = TurningUser.objects.get(email=usermail)
    except:
        userEmail = None
    if userEmail is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {"overlap":overlap}
    return JsonResponse(context)

def nickOverlapCheck(request):
    userNick = request.GET.get('nickName')
    try:
        userNickname = TurningUser.objects.get(nickName=userNick)
    except:
        userNickname = None
    if userNickname is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {"overlap":overlap}
    return JsonResponse(context)

def saveTodoList(request):
    todo = Todolist()
    saveTodo = request.GET.get('todoBody')
    todo.todoBody = saveTodo
    todo.save()
    return redirect('todolist')
    

