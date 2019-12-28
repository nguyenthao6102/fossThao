# from django.views.generic import ListView, DetailView
# # from blog.models import Post, Comment
# Create your views here.
# def list(request):
#     Data = {'Posts': Post.objects.all().order_by("-date")}
#     return render(request, 'blog/blog.html', Data)
# class PostListView(ListView):
#     queryset = Post.objects.all().order_by("-date")
#     template_name = 'blog/blog.html'
#     context_object_name = 'Posts'
#     paginate_by = 10
# def post(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'blog/post.html', {'post': post})
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post.html'
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)#Lấy bài viết từ Post với khóa ngoài là pk, 
    #nếu ko có trả về lỗi 404
    form = CommentForm()#Khởi tạo, gọi hàm __init__
    #Xử lý khi có bình luận
    if request.method == 'POST':
        #Đưa tác giả và bài viết vào trong form
        form = CommentForm(request.POST,author=request.user,post=post)
        if form.is_valid():
            #Kiểm tra nếu hợp lệ thì save lại
            form.save()
            return HttpResponseRedirect(request.path)
    #Đưa bài viết và form và template post.html
    return render(request, "blog/post.html", {"post":post, "form":form})