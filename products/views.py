from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "products/list.html", context)


def post_detail(request, post_id):
    posts = get_object_or_404(Post, pk=post_id)
    context = {
        "posts": posts
    }
    return render(request, "products/detail.html", context)


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("products/detail", post.id)
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "products/create.html", context)

# @login_required
# @require_POST
def delete(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
    return redirect("products/list")
#
#
# @login_required
# @require_http_methods(["GET", "POST"])
def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            article = form.save()
            return redirect("products/detail", article.pk)
    else:
        form = PostForm(instance=post)
    context = {
        "form": form,
        "posts": post,
    }
    return render(request, "products/create.html", context)
