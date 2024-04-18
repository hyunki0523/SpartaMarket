from django import forms
from products import models
from .models import Post, Comment
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"
        exclude = ['author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("post", "user")
