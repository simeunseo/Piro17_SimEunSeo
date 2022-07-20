from django.conf import settings
from django.db import models
from django.utils import timezone

class Tool(models.Model):
    #이름, 종류, 설명
    name = models.CharField(max_length=50, verbose_name="이름")
    type = models.CharField(max_length=50, verbose_name="종류")
    description = models.TextField(verbose_name="설명")

class Idea(models.Model):
    #아이디어명, 이미지, 아이디어 설명, 아이디어 관심도, 예상 개발툴
    name = models.CharField(max_length=50, verbose_name="이름")
    image = models.ImageField(blank=True, upload_to='ideas/%y%m%d', verbose_name="이미지")
    description = models.TextField(verbose_name="설명")
    interest = models.IntegerField(verbose_name="관심도")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes_user')
    # tool = models.CharField(max_length=50, verbose_name="개발툴", null=True)
    def count_likes_user(self): # total likes_user
        return self.likes_user.count()

    def __str__(self):
        return self.title
    
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='idea_tool')
    
class IdeaStar(models.Model):
    idea_name = models.CharField(max_length=50, verbose_name="아이디어명")