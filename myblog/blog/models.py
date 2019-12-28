from django.db import models
from django.conf import settings

# Create your models here.
#Tạo ra class Post để thiết kể ra bảng lưu các trường của bài viết
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    
    def __str__(self):
        return self.title
#Tạo ra class Comment để thiết kế ra bảng comment
class Comment(models.Model):
#Khi xóa bài viết thì xóa luôn bình luận
#ForeignKey biểu thị cho quan hệ một nhiều, mỗi bình luận chỉ ám chỉ cho một bài viết
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#Gọi user models, khi xóa user thì xóa luôn bình luận
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#Chứa nội dung bình luận
    body = models.TextField()
#Ngày giờ viết bình luận
    date = models.DateTimeField(auto_now_add=True)