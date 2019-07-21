from django.db import models
#UserModel -> Customizing
from django.contrib.auth.models import AbstractUser

#New User Class Name
class TurningUser(AbstractUser):
  #Necessary Table
  # 1. Army 2. Name 3. PW 4. E-mail 5. Phone Number
  # Name, E-mail, PW is already existed in User base Model
  # 1.Army Status > User has one ARMY_STATUS for classification
  ARMY_STATUS=(
    ("A","육군"),
    ("N","해군"),
    ("M","해병대"),
    ("AF","공군"),
    ("PSW","사회복무요원"),
    ("CP","의무 경찰"),
    ("CFF","의무 소방"),
    ("K","카투사"),
  )
  #On website for choosing user's army status
  userArmyStatus = models.CharField(max_length=20,choices=ARMY_STATUS,blank=False,default='A')
  #5. Phone Number > default value 'Null'
  tnPhoneNumb = models.PositiveIntegerField(default=0)
