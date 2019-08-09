from django.contrib import admin
from .models import DiaryForm, Todolist

# Register your models here.
admin.site.register(DiaryForm)
admin.site.register(Todolist)