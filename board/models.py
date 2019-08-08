from django.db import models
from turningaccounts.models import TurningUser
# Create your models here.

class Notice(models.Model):
    #글의 원주인을 정해주기 위해서 ForeignKey를 사용하여 TurningUser모델의 User값을 가지고 옴
    tnUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,related_name='turningUser',null=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    postHit=models.PositiveIntegerField(default=0) # 조회수 체크 - 정수를 인수로 받음
    userLikeName = models.ManyToManyField(TurningUser,related_name='nlikes')
    # like_count = models.PositiveIntegerField(default=0)
    # userLike = models.CharField(max_length=30,blank=True)
    # likePoint = models.ManyToManyField(TurningUser, blank=True)

    def __str__(self):
        return self.title
    
    def update_counter(self):
        self.postHit = self.postHit + 1
        self.save()

    @property
    def totalLike(self):
        return self.userLikeName.count()

class Noticecomment(models.Model):
    #글의 원주인을 정해주기 위해서 ForeignKey를 사용하여 TurningUser모델의 User값을 가지고 옴
    noticeCommentUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,null=True)
    notice = models.ForeignKey(Notice,on_delete=models.CASCADE,related_name="comments") # 부모모델을 소문자로 쓴다 - 그 키의 값을 가지고 온다.
    # on_delete=models.CASCADE는 이 글이 삭제될 때에 댓글들도 다 같이 삭제된다는 뜻 - CASCADE 말고 SET NULL, NO ACTION, SET DEFAULT, RESTRICT등이 올 수 있다!
    # related_name은 우리가 urls.py에서 name='~' 이라고 하는것과 같다! 그거를 가지고 오고 싶을때 이런 이름으로 부르겠다는 뜻
    commentdate=models.DateTimeField(auto_now=True, null=True) # 'date published'와 auto_now=True는 같음
    # null=True는 앞에 있는 변수명을 바꿨을 때 
    commentbody=models.TextField() # textfield가 작성할 수 있는(저장할 수 있는) 크기가 훨씬 큼

    def __str__(self):
        return self.commentbody



class Free(models.Model):
    tnUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,related_name='tnFreeUser',null=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    postHit=models.PositiveIntegerField(default=0) # 조회수 체크 - 정수를 인수로 받음
    #좋아요를 알기 위해서 다대다 모델을 걸어줍니다.
    userLikeName = models.ManyToManyField(TurningUser,related_name='flikes')
    

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.postHit = self.postHit + 1
        self.save()

    @property
    def totalLike(self):
        return self.userLikeName.count()

class Freecomment(models.Model):
    tnFreeCommentUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,null=True)
    free = models.ForeignKey(Free,on_delete=models.CASCADE,related_name="comments") # 부모모델을 소문자로 쓴다 - 그 키의 값을 가지고 온다.
    # on_delete=models.CASCADE는 이 글이 삭제될 때에 댓글들도 다 같이 삭제된다는 뜻 - CASCADE 말고 SET NULL, NO ACTION, SET DEFAULT, RESTRICT등이 올 수 있다!
    # related_name은 우리가 urls.py에서 name='~' 이라고 하는것과 같다! 그거를 가지고 오고 싶을때 이런 이름으로 부르겠다는 뜻
    commentdate=models.DateTimeField(auto_now=True, null=True) # 'date published'와 auto_now=True는 같음
    # null=True는 앞에 있는 변수명을 바꿨을 때 
    commentbody=models.TextField() # textfield가 작성할 수 있는(저장할 수 있는) 크기가 훨씬 큼

    def __str__(self):
        return self.commentbody



class Develop(models.Model):
    tnUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,related_name='tnDevelopUser',null=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    postHit=models.PositiveIntegerField(default=0) # 조회수 체크 - 정수를 인수로 받음
    userLikeName = models.ManyToManyField(TurningUser,related_name='dlikes')

    def __str__(self):
        return self.title

    def update_counter(self):
        self.postHit = self.postHit + 1
        self.save()

    @property
    def totalLike(self):
        return self.userLikeName.count()

class Developcomment(models.Model):
    tnDevelopCommentUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,null=True)
    develop = models.ForeignKey(Develop,on_delete=models.CASCADE,related_name="comments") # 부모모델을 소문자로 쓴다 - 그 키의 값을 가지고 온다.
    # on_delete=models.CASCADE는 이 글이 삭제될 때에 댓글들도 다 같이 삭제된다는 뜻 - CASCADE 말고 SET NULL, NO ACTION, SET DEFAULT, RESTRICT등이 올 수 있다!
    # related_name은 우리가 urls.py에서 name='~' 이라고 하는것과 같다! 그거를 가지고 오고 싶을때 이런 이름으로 부르겠다는 뜻
    commentdate=models.DateTimeField(auto_now=True, null=True) # 'date published'와 auto_now=True는 같음
    # null=True는 앞에 있는 변수명을 바꿨을 때 
    commentbody=models.TextField() # textfield가 작성할 수 있는(저장할 수 있는) 크기가 훨씬 큼

    def __str__(self):
        return self.commentbody