from django.db import models

# Create your models here.
class Feed(models.Model):
    # 속성들
    content = models.TextField()
    image = models.TextField()
    profile = models.TextField()
    nickname = models.TextField()
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)
    # 자동으로 지금 시간 넣기
    created_at = models.DateTimeField(auto_now_add=True)
    # 자동으로 지금 시간
    updated_at = models.DateTimeField(auto_now=True)

    # 출력 형태 지정
    def __str__(self):
        return self.content

    # 내용의 길이 반환 함수 생성
    def content_length(self):
        return len(self.content)
    content_length.short_discription = '글자수'