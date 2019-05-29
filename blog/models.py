from django.db import models
from django.utils import timezone


class Post(models.Model):#Post是一個django模型
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#指向另一個模型的連接。
    title = models.CharField(max_length=200)#用為數有限的字符來定義一個文本
    text = models.TextField()#這是沒有長度限制的長文本
    created_date = models.DateTimeField(
            default=timezone.now)#這是日期和時間。
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title