from django.db import models
from turningaccounts.models import TurningUser

# Create your models here.

class DiaryForm(models.Model):
  tnUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,null=True)
  diaryBody = models.TextField()
  diaryDate = models.DateField()
  def summary(self):
    return self.diaryBody[:100]


class Todolist(models.Model):
  tnUser = models.ForeignKey(TurningUser,on_delete=models.CASCADE,null=True)
  todoBody = models.TextField()
  checkTodo = models.BooleanField(default=False)

  def __str__(self):
    return self.todoBody
  


