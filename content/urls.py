from django.urls import path
from .views import Main
from .views import Post

app_name = 'content'

urlpatterns = [
    # first url에서 content url로 가져온다.
    path('main/', Main.as_view(), name='main'),
    path('main/post/', Post.as_view(), name='post'),
]