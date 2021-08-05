from django.db import models

photo = models.ImageField(blank=True)

class Journalist(models.Model):
    def __str__(self):
        return self.name # 저널리스트 이름 OBJESTS가 아닌 지정한 이름으로 나오게 하기
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    journallist = models.ForeignKey(Journalist,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Journalist,on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)