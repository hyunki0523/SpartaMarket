from django import forms
from products import models
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"