from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from .models import Post
urlpatterns = [
    # path('',views.PostListView.as_view(), name='blog'),
    path('', ListView.as_view(
        #sắp xếp blog mới hiển thị lên dầu trang, theo thứ tự từ mới đến cũ
        queryset = Post.objects.all().order_by("-date"),
        template_name = 'blog/blog.html',
        context_object_name = 'Posts',
        #Trang hiển thị 10 bài viết, nếu hơn thì hiển thị tiếp theo
        paginate_by =5)
        ,name='blog'),
    path('<int:pk>/', views.post, name='post'),#gọi hàm post trong views
]