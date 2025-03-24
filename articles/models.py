from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):  # 댓글 생성
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 위의 article모델과 comment모델이 동일함
    # 게시물을 지웠으면 그 게시물에 존재했던 댓글은 당연히 지워진다. -> 이 개념이 CASCADE