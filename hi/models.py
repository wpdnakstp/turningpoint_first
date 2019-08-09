from django.db import models
from turningaccounts.models import TurningUser

# Create your models here.

class DiaryForm(models.Model):
  tnUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,null=True)
  diaryTitle = models.CharField(max_length=200)
  diaryBody = models.TextField()
  diaryDate = models.DateField(auto_now_add=True)


class Todolist(models.Model):
  todoBody = models.TextField()

  def __str__(self):
    return self.todoBody