from django.urls import path
from .views import Delete, Main, Modify, isliked
from .views import Post

app_name = 'content'

urlpatterns = [
    # content url을 설정한다.
    path('main/', Main.as_view(), name='main'),
    path('main/post/', Post.as_view(), name='post'),
    # <int:pk>는 변수 지정, 정수인 pk=id를 이용함
    path('main/post/<int:pk>', Modify.as_view(), name='modify'),
    path('main/delete/<int:pk>', Delete, name='delete'),
    path('main/isliked/<int:pk>', isliked, name='isliked'),
]