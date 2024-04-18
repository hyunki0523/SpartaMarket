from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST


# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "products/list.html", context)


def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    comments = posts.comments.all().order_by("-pk")
    context = {
        "posts": posts,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "products/detail.html", context)



def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post:detail", post.id)
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "products/create.html", context)

@login_required
@require_POST
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        if post.author == request.user:
            post = get_object_or_404(Post, pk=pk)
            post.delete()
    return redirect("post:list")

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                article = form.save()
                return redirect("post:detail", post.id)
        else:
            form = PostForm(instance=post)
    else:
        return redirect("post:list")

    context = {
        "form": form,
        "post": post,
    }
    return render(request, "products/update.html", context)

@require_POST
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user

        # comment.post_id = pk
        # print("comment.post_id:", comment.post_id)
        comment.save()

        return redirect("post:detail", post.pk)


@require_POST
def comment_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect("post:detail", pk)