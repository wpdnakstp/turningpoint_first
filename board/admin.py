from django.contrib import admin
from .models import Notice, Free, Develop, Noticecomment, Freecomment, Developcomment

# Register your models here.
admin.site.register(Notice)
admin.site.register(Free)
admin.site.register(Develop)
admin.site.register(Noticecomment)
admin.site.register(Freecomment)
admin.site.register(Developcomment)