from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
#Hàm khởi tạo để sinh ra tác 
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
#Overide lại hàm save để đưa tác giả và bài viết vào ComentForm
    def save(self, commit=True):
        comment = super().save(commit=False)#chưa lưu vào database
        comment.author = self.author
        comment.post = self.post
        comment.save()#Lưu vào database khi đã thêm author và post vào comment
#CommentForm tạo ra input(phần body) để nhập model của comment
    class Meta:
        model = Comment
        fields = ["body"]