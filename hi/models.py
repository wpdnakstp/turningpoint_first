from django.db import models
from turningaccounts.models import TurningUser

# Create your models here.

class DiaryForm(models.Model):
  tnUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,null=True)
  diaryBody = models.TextField()
  diaryDate = models.DateField(auto_now_add=True)
  
  def summary(self):
    return self.diaryBody[:100]


class Todolist(models.Model):
  todoBody = models.TextField()

  def __str__(self):
    return self.todoBody
  diaryDate = models.DateField()


