from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import Feed 
# Create your views here.

# 읽기 - Read
class Main(APIView):
    def get(self, request):
        # 모든 피드를 불러온다.
        feed_list = Feed.objects.all()

        # 피드를 하나씩 대상으로 출력한다.
        for feed in feed_list:
            # 오류 테스트하기 좋은 print
            print(feed)
        
        # 피드 리스트를 렌더링한다.
        return render(request, "content/main.html", {
            'feed_list': feed_list,
        })

# 쓰기 - Write
class Post(APIView):
    # 요청을 렌더링한다.
    def get(self, request):
        return render(request, "content/post.html")
    
    def post(self, request):
        # main.html 에서 이름이 같은 데이터를 가져온다.
        content = request.POST.get('content')
        nickname = request.POST.get('nickname')
        image = request.POST.get('image')
        profile = request.POST.get('profile')

        feed = Feed()
        feed.content = content
        feed.nickname = nickname
        feed.image = image
        feed.profile = profile
        feed.save()

        return redirect('content:main')

# 고치기 - Modify
class Modify(APIView):
    def post(self, request, pk):
        # main.html 에서 이름이 같은 데이터를 가져온다.
        content = request.POST.get('content')
        nickname = request.POST.get('nickname')
        image = request.POST.get('image')
        profile = request.POST.get('profile')

        #id=pk인 모든 피드를 불러온다.
        feed = Feed.objects.get(id=pk)
        feed.content = content
        feed.nickname = nickname
        feed.image = image
        feed.profile = profile
        feed.save()

        # content의 메인으로 되돌린다.
        return redirect('content:main')
    
    def get(self, request, pk):
        feed = Feed.objects.get(id=pk)
        # modify.html의 요청에 피드를 반환한다.(수정을 위한 데이터 전달)
        return render(request, "content/modify.html", {
            'feed': feed,
        })